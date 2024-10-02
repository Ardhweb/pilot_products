from django.shortcuts import render

# Create your views here.
import os
import hmac
import hashlib
import json
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test

@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def github_webhook(request):
    secret = os.getenv('GITHUB_WEBHOOK_SECRET').encode()  # Retrieve the secret from the environment
    signature = request.headers.get('X-Hub-Signature-256', '').encode()

    # Verify the signature
    mac = hmac.new(secret, msg=request.body, digestmod=hashlib.sha256)
    if not hmac.compare_digest(b'sha256=' + mac.hexdigest().encode(), signature):
        return JsonResponse({'error': 'Invalid signature'}, status=403)

    payload = json.loads(request.body)
    action = payload.get('action')

    if action in ['opened', 'synchronize']:
        repo_dir = '/home/pilotprojects/pilot_products/'  # Change to your repo path
        branch_name = 'production'  # Specify the branch you want to pull

        try:
            # Change directory to your repository
            os.chdir(repo_dir)

            # Fetch the latest changes and pull from the specified branch
            result = subprocess.run(['git', 'fetch', 'origin', branch_name], capture_output=True, text=True)
            if result.returncode != 0:
                return JsonResponse({'error': 'Git fetch failed'}, status=500)

            result = subprocess.run(['git', 'checkout', branch_name], capture_output=True, text=True)
            if result.returncode != 0:
                return JsonResponse({'error': 'Git checkout failed'}, status=500)

            result = subprocess.run(['git', 'pull', 'origin', branch_name], capture_output=True, text=True)
            if result.returncode != 0:
                return JsonResponse({'error': 'Git pull failed'}, status=500)

            # Optionally log the output
            print(result.stdout)
            print(result.stderr)

        except Exception as e:
            print(f"Error pulling repository: {str(e)}")
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'status': 'success'}, status=200)

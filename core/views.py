from django.shortcuts import render
import os
import hmac
import hashlib
import json
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def github_webhook(request):
    secret = os.getenv('GITHUB_WEBHOOK_SECRET').encode()
    signature = request.headers.get('X-Hub-Signature-256', '').encode()

    # Log incoming request details for debugging
    print(f"Request body: {request.body.decode()}")
    print(f"Headers: {request.headers}")

    # Verify the signature
    mac = hmac.new(secret, msg=request.body, digestmod=hashlib.sha256)
    computed_signature = b'sha256=' + mac.hexdigest().encode()

    if not hmac.compare_digest(computed_signature, signature):
        print(f"Computed signature: {computed_signature}")
        print(f"Received signature: {signature}")
        return JsonResponse({'error': 'Invalid signature'}, status=403)

    # Proceed with deployment logic for any push event
    repo_dir = '/home/pilotprojects/pilot_products/'
    try:
        os.chdir(repo_dir)
        subprocess.run(['git', 'fetch', 'origin'], check=True)
        subprocess.run(['git', 'checkout', 'main'], check=True)  # Switch to main branch
        subprocess.run(['git', 'pull', 'origin', 'main'], check=True)  # Pull latest changes
    except subprocess.CalledProcessError as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'status': 'success'}, status=200)

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import subprocess

@csrf_exempt
def github_webhook(request):
    if request.method == 'POST':
        repo_dir = '/home/pilotprojects/pilot_products/'
        try:
            os.chdir(repo_dir)
            subprocess.run(['git', 'fetch', 'origin'], check=True)
            subprocess.run(['git', 'checkout', 'main'], check=True)
            subprocess.run(['git', 'pull', 'origin', 'main'], check=True)
            return JsonResponse({'status': 'success'}, status=200)
        except subprocess.CalledProcessError as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


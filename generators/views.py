from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
def password_gen(request):

    if request.method == 'POST':
        # Generate a random password of desired length
        password_length = int(request.POST.get('password_length', 12))
        password = get_random_string(length=password_length)
        return render(request,'generator/password_generator.html', {'password': password})
    else:
        return render(request,'generator/password_generator.html')
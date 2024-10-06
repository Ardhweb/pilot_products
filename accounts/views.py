from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import LoginForm
def logout_user(request):
    logout(request)  # Log the user out
    # # Get the HTTP_REFERER from the request headers
    # referer = request.META.get('HTTP_REFERER')
    # # If referer exists, redirect to it, otherwise redirect to home
    # if referer:
    #     return HttpResponseRedirect(referer)
    # else:
    #     return redirect('home')  # Fallback to a default page
    return redirect('index')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm  # Ensure you have your LoginForm imported
from django.contrib.auth.models import User
def login_user(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            print(f"Authenticated user: {user}")  # Debug statement
            if user is not None and user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse("Authentication failed: User not found or inactive")
        else:
            return HttpResponse("Form is invalid")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


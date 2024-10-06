from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
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
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.error(request, "This account is disabled.")
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

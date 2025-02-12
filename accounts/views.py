from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import LoginForm,SignupForm
def logout_user(request):
    logout(request)  # Log the user out
    # # Get the HTTP_REFERER from the request headers
    # referer = request.META.get('HTTP_REFERER')
    # # If referer exists, redirect to it, otherwise redirect to home
    # if referer:
    #     return HttpResponseRedirect(referer)
    # else:
    #     return redirect('home')  # Fallback to a default page
    return redirect('cover-home')


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
                return redirect('cover-home')
            else:
                return HttpResponse("Authentication failed: User not found or inactive")
        else:
            return HttpResponse("Form is invalid")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        user_form = SignupForm(request.POST)
        if user_form.is_valid ():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            print(user_form.cleaned_data['password'])
            user = authenticate(request, email=user_form.cleaned_data['email'], password=user_form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('cover-home')
            else:
                return HttpResponse("User not Exist!")   
    else:
        user_form = SignupForm()
    return render(request,'accounts/register.html',{'user_form': user_form})

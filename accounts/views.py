from django.shortcuts import render, redirect
from accounts.forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(dash)
            else:
                messages.error(request, 'Username and password didn\'t matched.')

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = form.save(commit=False)
            user.set_password(data['password1'])
            user.save()
            login(request, user)
            return redirect('dash')

    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dash(request):
    
    return render(request, 'dash/dash.html', {})












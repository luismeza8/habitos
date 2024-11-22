from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm, LoginForm

def index(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = LoginForm(request, data=request.POST)
            register_form = RegisterForm()
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('home')
        elif 'register' in request.POST:
            register_form = RegisterForm(request.POST)
            login_form = LoginForm()
            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.set_password(register_form.cleaned_data['password'])
                user.save()
                login(request, user)
                return redirect('home')
    else:
        login_form = LoginForm()
        register_form = RegisterForm()

    return render(request, 'users/index.html', {'login_form': login_form, 'register_form': register_form})


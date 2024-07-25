from django.shortcuts import render, redirect
from .forms import LoginForm, CreateUserForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.


def login_page(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'user/login.html', context)

def sign_up(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.instance
            form.save()

            login(request, user)
            return redirect('home')

    context  ={
        'form': form
    }

    return render(request, 'user/sign_up.html', context)

def logout_page(request):
    logout(request)
    return redirect('home')



def profile(request, pk):

    return render(request, 'user/profile.html')


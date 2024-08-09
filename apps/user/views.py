from django.contrib.auth.password_validation import validate_password

from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from django.shortcuts import render, redirect
from .forms import LoginForm, CreateUserForm, UserForm

from .models import Subscription, User
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
    user = User.objects.get(id=pk)

    subscribers_count = Subscription.objects.filter(author=user).count()
    subscribtions_count = Subscription.objects.filter(user=user).count()
    
    subscribers = Subscription.objects.filter(author=user)
    subscribtions = Subscription.objects.filter(user=user)

    if request.user.is_authenticated:
        is_subscribed = Subscription.objects.filter(user=request.user, author=user).exists()
    else:
        is_subscribed = False


    form = UserForm(instance=user)
    if request.method == 'POST':
        if 'update_user' in request.POST:
            form = UserForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return redirect('profile', pk=user.id)

        if 'subscribe' in request.POST:
            if is_subscribed:
                Subscription.objects.filter(user=request.user, author=user).delete()
                return redirect('profile', pk=pk)
            else:
                Subscription.objects.create(user=request.user, author=user)
                return redirect('profile', pk=pk)
        
    context = {
        'form': form,
        'user': user,
        'is_subscribed': is_subscribed,
        'subscribers_count': subscribers_count,
        'subscribtions_count': subscribtions_count,
        'subscribers': subscribers,
        'subscribtions': subscribtions
    }
    return render(request, 'user/profile.html', context)





def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        confirm_password2 = request.POST.get('confirm_password2')

        user = request.user

        if new_password1 != confirm_password2:
            messages.error(request, 'Пароли не совпадают!')
            return render(request, 'user/rename_password.html')

        try:
            validate_password(new_password1)
            if user.check_password(old_password):
                user.set_password(new_password1)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Пароль успешно изменен!')
                return redirect('login')
            else:
                messages.error(request, 'Неверный старый пароль')
        except ValidationError as e:
            messages.error(request, e)

    return render(request, 'user/change_password.html')


from django.http import HttpResponseRedirect
from django.shortcuts import render
from users.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages
from users.models import User
from django.core.mail import send_mail

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.add_message(request, messages.INFO, f'{user} вы успешно вошли в аккаунт')
                return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Неправильный никнейм или пароль. Попробуйте еще раз', extra_tags='password_login ')
    else:
        form = UserLoginForm()
    context = {
        'title': 'Авторизация',
        'form': form,
    }

    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid() and (form.data['password1'] == form.data['password2']) and not(form.data['email'] in User.objects.all().values_list('email', flat=True)):
            form.save()
            send_mail(
                'Регистрация на сайте',
                'Вы успешно зарегистрировались на сайте. Ваш логин: {}, пароль: {}'.format(form.data['username'],
                                                                                           form.data['password1']),
                'fruit_test_db@mail.ru',
                [form.data['email']],
                fail_silently=False,
            )
            messages.add_message(request, messages.INFO, f'{form.data["username"]} вы успешно создали в аккаунт')
            return HttpResponseRedirect(reverse('user:login'))
        else:
            if form.data['username'] in User.objects.all().values_list('username', flat=True):
                messages.error(request, 'Никнейм занят. Введите другой', extra_tags="username")
            elif form.data['email'] in User.objects.all().values_list('email', flat=True):
                messages.error(request, 'Почта занята. Введите другую', extra_tags="email")
            elif form.errors.as_data() == {'password2'}:
                messages.error(request, 'Пароль короче 8 символов или содержит только цифры', extra_tags="password")
            elif form.data['password1'] != form.data['password2']:
                messages.error(request, 'Пароли не совпадают', extra_tags="passwords")
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Регистрация',
        'form': form,
    }

    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'title': 'Профиль пользователя',
    }

    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)

    return HttpResponseRedirect(reverse('home'))

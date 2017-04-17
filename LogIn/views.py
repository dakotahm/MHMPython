from django.shortcuts import render
from LogIn import models
from LogIn.forms import *
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render_to_response


def login(request, template_name):

    from .forms import LoginForm

    if request.method == 'POST':
        test = models.AuthUser.objects.all()
        print(test)
        print(request.POST)

        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/")

            else:
                return HttpResponse("Invalid login. Please try again.")

        else:
            print("Form not valid")

    else:
        form = LoginForm()

        print("blank login form")

    return render(request, 'LogIn/login.html',)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = models.AuthUser.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()

    return render_to_response('LogIn/register.html')


def register_success(request):
    return render_to_response(
        'LogIn/success.html',
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
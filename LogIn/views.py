from django.shortcuts import render
from LogIn import models
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect


# TODO: validate against Users in DB, not AuthUsers


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

    return render(request, 'LogIn/Login.html',)
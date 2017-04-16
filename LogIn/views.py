from django.shortcuts import render
from LogIn import models


def LoginView(request):
    def index(request):
        from .forms import LoginForm
        if request.method == 'POST':

            form = LoginForm(request.POST)
            print(request)
            print(request.POST)
            print()
            test = models.User.objects.all()
            print(test)

            if form.is_valid():
                print(request.POST)
                print(request.POST.get('value', -1))

            else:
                print("Form not valid")

        else:
            form = LoginForm()
            print("blank form")
        return render(request, 'RecordEvent/Record.html')

    return render(request,'LogIn/Login.html')
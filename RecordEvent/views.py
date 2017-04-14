from django.shortcuts import render
from RecordEvent import  models

def index(request):
    from .forms import LogForm
    if (request.method=='POST'):

        form=LogForm(request.POST)
        # print(request)
        # print(request.POST)
        # print()
        test=models.Entries.objects.all()
        print(test)

        if form.is_valid():
            print(request.POST)
            print(request.POST.get('value',-1))



        else:
            print("Form not valid")

    else:
        form=LogForm()
        print("blank form")
    return render(request,'RecordEvent/Record.html')

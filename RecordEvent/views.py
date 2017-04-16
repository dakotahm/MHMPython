from django.shortcuts import render
from RecordEvent import  models
from datetime import datetime,date

def index(request):
    from .forms import LogForm
    #hardcoded user1 for testing
    Measurables=[ entry for entry in models.Measurables.objects.all().filter(user_id=1)]

    if (request.method=='POST'):

        form=LogForm(request.POST)
        # print(request)
        # print(request.POST)
        # print()

        test=models.Entries.objects.all()
        print(test)
        print(request.POST)
        if form.is_valid():
            print(request.POST)
            print(request.POST.get('date',datetime.today().strftime('%Y-%m-%d')))
            print(request.POST.get('time', datetime.today().strftime('%H:%M:%S')))
            print(request.POST.get('log', ''))
            print(request.POST.get('location', ''))
            print(request.POST.get('value', -1))
            print(request.POST.get('measureId', '-1'))



        else:
            print("Form not valid")

    else:
        form=LogForm()
        print("blank form")
        #test = int('fail')

    return render(request,'RecordEvent/Record.html',{'dropdown':Measurables})

from django.shortcuts import render
from RecordEvent import  models
from datetime import datetime,date
import json

def index(request):
    from .forms import LogForm
    #hardcoded user1 for testing
    Measurables=[ entry for entry in models.Measurables.objects.all().filter(user_id=1)]

    if (request.method=='POST'):

        form=LogForm(request.POST)
        # print(request)
        print(request.POST)
        # print()

        test=models.Entries.objects.all()
        print(test)
        print(request.POST)
        if form.is_valid():
            print(request.POST)
            dateInput=request.POST.get('date',datetime.today()).split("/")
            timeInput=request.POST.get('time', datetime.today()).split(':')
            finalDatetime= datetime(int(dateInput[2]),int(dateInput[0]),int(dateInput[1]),int(timeInput[0]),int(timeInput[1]))
            log=request.POST.get('log', '')
            location=request.POST.get('location', '')
            value=request.POST.get('value', -1)
            measureID=request.POST.get('measureId', '-1')

            toJson={'log':log,'value':value,'location':location}
            newEntry = models.Entries(parent=measureID,timestamp=finalDatetime,data=json.dumps(toJson))



        else:
            print("Form not valid")

    else:
        form=LogForm()
        print("blank form")
        #test = int('fail')

    return render(request,'RecordEvent/Record.html',{'dropdown':Measurables})

def insertMeasurable(request):
    if (request.method == 'POST'):
        print(request.POST)
        minInput=request.POST.get('min',0);
        maxInput=request.POST.get('max',100)
        nameInput=request.POST.get('name','name')
        newMeasurable=models.Measurables(name=nameInput,max=int(maxInput),min=int(minInput),user_id=1)
    return render(request,'RecordEvent/AddMeasurable.html')

from django.shortcuts import render
from RecordEvent import  models
from datetime import datetime,date
from django.contrib.auth.decorators import login_required
from django.contrib import auth


@login_required
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
            dateInput=request.POST.get('date',datetime.today().strftime('%Y-%m-%d'))
            timeInput=request.POST.get('time', datetime.today().strftime('%H:%M:%S'))
            log=request.POST.get('log', '')
            location=request.POST.get('location', '')
            value=request.POST.get('value', -1)
            measureID=request.POST.get('measureId', '-1')

            # if dateInput.isspace() and timeInput.isspace():
            #     theTime=datetime.now()
            # elif not dateInput.isspace() and not timeInput.isspace():
            #     theTime=datetime.strptime(dateInput+' '+timeInput, "%m/%d/%Y %I:%M:%S %p")
            # elif not dateInput.isspace() and  timeInput.isspace():
            #     theTime=datetime.strptime(dateInput+' '+timeInput, "%m/%d/%Y")
            # elif dateInput.isspace() and not timeInput.isspace():
            #     theTime=datetime.strptime(timeInput, "%I:%M:%S %p")
           # newEntry = models.Entries(parent=measureID,timestamp=theTime,value=)

        # class Entries(models.Model):
        #     id = models.BigAutoField(primary_key=True)
        #     parent = models.BigIntegerField()
        #     data = models.CharField(max_length=20000)
        #     timestamp = models.DateTimeField(blank=True, null=True)

        else:
            print("Form not valid")

    else:
        form=LogForm()
        print("blank form")
        #test = int('fail')

    return render(request,'RecordEvent/Record.html',{'dropdown':Measurables})


@login_required
def insertMeasurable(request):
    return render(request,'RecordEvent/AddMeasurable.html')

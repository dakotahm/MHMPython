from django.shortcuts import render
from RecordEvent import  models
from datetime import datetime,date
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import LogForm,ValidateRecordEvent,ValidateNewLog

@login_required
def index(request):


    # code for current userid
    current_user = request.user
    print(current_user)
    print(current_user.id)

    #hardcoded user1 for testing
    Measurables=[ entry for entry in models.Measurables.objects.all().filter(user_id=current_user.id)]

    if (request.method=='POST'):
        form=LogForm(request.POST)
        test=models.Entries.objects.all()
        print(request.POST)

        dateInput=request.POST.get('date',datetime.today().strftime('%Y-%m-%d'))
        timeInput=request.POST.get('time', datetime.today().strftime('%H:%M:%S'))
        log=request.POST.get('log', '')
        location=request.POST.get('location', '')
        value=request.POST.get('value', -1)
        measureID=request.POST.get('measureId', '-1')
        validate=ValidateRecordEvent(dateInput,timeInput,log,int(value),int(measureID),current_user.id,location)
        if not validate.ValidateAndSave:
            #handle error and proceed
            pass



    else:
        form=LogForm()
        print("blank form")
        #test = int('fail')

    return render(request,'RecordEvent/Record.html',{'dropdown':Measurables})


@login_required
def insertMeasurable(request):
    if (request.method == 'POST'):
        print(request.user.id)
        name = request.POST.get('name', '')
        maxInput = request.POST.get('max', -1)
        minInput = request.POST.get('min', -1)
        type = request.POST.get('measureId', '')
        validate=ValidateNewLog(name,int(maxInput),int(minInput),request.user.id,type)
        if not validate.ValidateAndAddMeasurable:
            #handle failure
            pass

    return render(request,'RecordEvent/AddMeasurable.html')
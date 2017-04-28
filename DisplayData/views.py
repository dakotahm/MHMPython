from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from DisplayData import models
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from DisplayData import LogFunctions
from chartit import DataPool, Chart

import json

#from .forms import SubmitIDForm
from RecordEvent.forms import LogForm,ValidateRecordEvent,ValidateNewLog


@login_required
def DisplayView(request):
    measurables = [entry for entry in models.Measurables.objects.all().filter(user_id=request.user.id)]
    return render(request,'DisplayData/Display.html',{'dropdown':measurables})


def get_data(request, *args, **kwargs):

    #Here is the measurable Id and time (in python datetime from the form!!!!!!!!!!!!!!!!!!
    print(request.GET)
    mId=request.GET['measurableId']
    timeframe = LogFunctions.gettime(request.GET['timeframe'])
    print(mId)
    print(timeframe)

    all_measurables= models.Measurables.objects.all().filter(user_id=request.user.id)
    all_entries = models.Entries.objects.all().filter(parent=mId).filter(timestamp__gte=timeframe)

    print(all_entries)

    all_ids = []
    for m in all_measurables:
        all_ids.append(m.id)
    print(all_ids)

    display_name = ''
    for m in all_measurables:
        if m.id == mId:
            display_name = m.name

    print(display_name)

    all_times = []

    for m in all_entries:
        time = m.timestamp
        print(time)
        formatted_time = time.strftime("%b %d %Y %H:%M:%S")
        all_times.append(formatted_time)

    all_data = []
    for m in all_entries:
        data = m.data
        json_data = json.loads(data)
        value = json_data['value']
        all_data.append(value)

    bg_color = "rgba(117, 201, 196, 0.5)"

    data = {
        "labels": all_times,
        "default": all_data,
        "name": display_name,
        "bgcolor": bg_color
    }   

    return JsonResponse(data)
    '''
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)
    '''


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

   # got_data = get_data(request)
   # print(got_data)
    
    def get(self, request, format=None):

        all_measurables=[entry for entry in models.Measurables.objects.all().filter(user_id=request.user.id)]

        

    

        #all_entries = models.Entries.objects.all().filter(parent=2) #change to input from textfield or change to 2
        all_entries = models.Entries.objects.all().filter(parent=2)
        all_id = models.Entries.objects.all().values_list('id', flat=True)
        
        
        all_ids = [m.id for m in all_measurables] #use this to make drop down
        
        all_times = [m.timestamp for m in all_entries]

        all_data = []
        for m in all_entries:
            data = m.data
            json_data = json.loads(data)
            value = json_data['value']
            all_data.append(value)

        
        data = {
            "labels": all_times,
            "default": all_data,
        }   
        return Response(data)

@login_required
def LogDisplay(request):
    measurables=[entry for entry in models.Measurables.objects.all().filter(user_id=request.user.id)]
    if (request.method == 'POST' and request.is_ajax()):

       #data can be accessed from this post request and processed here
        mID=int(request.POST.get('measuraleId'))
        timeframe=LogFunctions.gettime(request.POST.get('timeframe'))
        onSuccess={'html':LogFunctions.buildHTML(mID,timeframe)}
        print(onSuccess)
        return HttpResponse(json.dumps(onSuccess), content_type="application/json")


    return render(request, 'DisplayData/Logs.html',{'dropdown':measurables})


@login_required
def DropdownDisplay(request):
    measurables=[entry for entry in models.Measurables.objects.all().filter(user_id=request.user.id)]
    if (request.method == 'POST' and request.is_ajax()):

       #data can be accessed from this post request and processed here
        print(request.POST)

    return render(request, 'DisplayData/Display.html',{'dropdown':measurables})





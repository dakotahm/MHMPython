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
    return render(request,'DisplayData/Display.html')


def get_data(request, *args, **kwargs):

    all_measurables=[entry for entry in models.Measurables.objects.all().filter(user_id=request.user.id)]
    #all_entries = models.Entries.objects.all().filter(parent=2) #change to input from textfield or change to 2
    all_entries = models.Entries.objects.all().filter(parent=2)

    
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

    def get(self, request, format=None):
        
        all_measurables=[entry for entry in models.Measurables.objects.all().filter(user_id=request.user.id)]

        #all_entries = models.Entries.objects.all().filter(parent=2) #change to input from textfield or change to 2
        all_entries = models.Entries.objects.all().filter(parent=2)
        
        #all_times = [m.timestamp for m in all_entries]
        all_times =[]
        all_data = []

        
        for row in all_entries:
            data = row.data
            json_data= json.loads(data)
            value= json_data['value']
            all_data.append(value)
            all_times.append(row.timestamp)
        

        '''
        for m in all_entries:
            data = m.data
            json_data = json.loads(data)
            value = json_data['value']
            all_data.append(value)
        '''
        
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
        mID = int(request.POST.get('measuraleId'))
        timeframe=GraphFunctions.gettime(request.POST.get('timeframe'))
        data = GraphFunctions.getRows(mID, timeframe)

        print(data)

        return Response(data)


    return render(request, 'DisplayData/Dropdown.html',{'dropdown':measurables})






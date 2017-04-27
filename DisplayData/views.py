from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from DisplayData import models
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from DisplayData import LogFunctions
from chartit import DataPool, Chart
from rest_framework.permissions import IsAuthenticated
import random

import json

#from .forms import SubmitIDForm
from RecordEvent.forms import LogForm,ValidateRecordEvent,ValidateNewLog


@login_required
def DisplayView(request):
    return render(request,'DisplayData/Display.html')

#using this now
def get_data(request, *args, **kwargs):


    print(request.user.id)
        
    all_measurables= models.Measurables.objects.all().filter(user_id=request.user.id)

    #debug
    all_ids = []
    for m in all_measurables:
        all_ids.append(m.id)
    print(all_ids)
    #end_debug

    display_id = random.choice(all_ids)
    
    all_entries = models.Entries.objects.all().filter(parent=display_id) #user input goes here

    #debug
    all_ents = []
    for m in all_entries:
        all_ents.append(m.id)
    print(all_ents)
    #end_debug
    

    all_times = []
    all_data = []

    
    for row in all_entries:
        data = row.data
        json_data= json.loads(data)
        value= json_data['value']
        all_data.append(value)
        all_times.append(row.timestamp)
    
    data = {
        "labels": all_times,
        "default": all_data,
    }   
    
    return JsonResponse(data)


#ignore the following
class ChartData(APIView):
    authentication_classes = []
    permission_classes = [IsAuthenticated, ]


    def get(self, request, format=None):

        print(self.request.user)
        
        all_measurables= models.Measurables.objects.all()

        #print(all_measurables)

        
        all_ids = []
        for m in all_measurables:
            all_ids.append(m.id)
        print(all_ids)
        

        #all_entries = models.Entries.objects.all().filter(parent=2) #change to input from textfield or change to 2
        all_entries = models.Entries.objects.all().filter(parent=4)

        all_ents = []
        for m in all_entries:
            all_ents.append(m.id)
        print(all_ents)
        
        #all_times = [m.timestamp for m in all_entries]
        all_times = []
        all_data = []

        
        for row in all_entries:
            data = row.data
            json_data= json.loads(data)
            value= json_data['value']
            all_data.append(value)
            all_times.append(row.timestamp)
        
        data = {
            "labels": all_times,
            "default": all_data,
        }   
        
        return Response(data)



@login_required
def LogDisplay(request):
    measurables=[entry for entry in models.Measurables.objects.all().filter(user_id=request.user.id)]

    print(request.user.id)

    all_ids = []
    for m in measurables:
        all_ids.append(m.id)
    print(all_ids)

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


    return render(request, 'DisplayData/Display.html',{'dropdown':measurables})






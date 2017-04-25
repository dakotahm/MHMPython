from django.shortcuts import render
from django.http import JsonResponse
from DisplayData import models


from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

from chartit import DataPool, Chart

import json

from RecordEvent.forms import LogForm,ValidateRecordEvent,ValidateNewLog


@login_required
def DisplayView(request):
    return render(request,'DisplayData/Display.html')


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)



def index(request):
    return render(request, 'form.html')

display_index = 0

def search(request):
    if request.method == 'POST':
        search_id = request.POST['textfield']
        print(search_id)
        display_index = search_id
    else:
        return render(request, 'form.html')   


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        display_id = request.POST.get("textfield", "")
        display_id = int(display_id)

        all_entries = models.Entries.objects.all().filter(parent=display_id) #change to input from drop down or change to 2
        all_id = models.Entries.objects.all().values_list('id', flat=True)
        all_measurables = models.Measurables.objects.all().filter(user_id=request.user.id) #change to current user
        
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

    return render(request, 'DisplayData/Logs.html',{'dropdown':measurables})




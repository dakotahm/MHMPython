from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from TreatmentAid import  models
from django.db.models import Q
import json
from django.http import HttpResponse


@login_required
def AidView(request):

    # code for current userid
    current_user = request.user
    print(current_user)
    print(current_user.id)

    Downloadables = [down for down in models.Treatmentdownloads.objects.all().filter(Q(userfk=current_user.id) | Q(global_field=1))]

    #if(request.method=='GET' and request.is_ajax()):
        #puts all the get parameters in a list
        #for some reason the key 'url' was not working
        #theURL=[request.GET[key] for key in request.GET][0]

        #response = HttpResponse("README.txt")
        #response['Content-Type'] = 'text/plain'
        #response['Content-Disposition'] = 'attachment; filename=README.txt'
        #return response


    return render(request,'TreatmentAid/Aid.html',{'download':Downloadables})

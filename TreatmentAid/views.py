from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from TreatmentAid import  models
from django.db.models import Q
import json
from django.http import HttpResponse


@login_required
def AidView(request):
    '''handles request and populates Downloadables dictionary'''

    # code for current userid
    current_user = request.user
    print(current_user)
    print(current_user.id)

    Downloadables = [down for down in models.Treatmentdownloads.objects.all().filter(Q(userfk=current_user.id) | Q(global_field=1))]

    return render(request,'TreatmentAid/Aid.html',{'download':Downloadables})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def AidView(request):
    return render(request,'TreatmentAid/Aid.html')
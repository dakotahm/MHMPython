from django.shortcuts import render

def AidView(request):
    return render(request,'TreatmentAid/Aid.html')
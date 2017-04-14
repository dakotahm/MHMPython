from django.shortcuts import render

def DisplayView(request):
    return render(request,'DisplayData/Display.html')
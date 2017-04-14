from django.shortcuts import render

def index(request):
    from .forms import LogForm
    if (request.method=='POST'):

        form=LogForm(request.POST)

        if form.is_valid():
            print(form.valueText)

    else:
        form=LogForm()
    return render(request,'RecordEvent/Record.html')

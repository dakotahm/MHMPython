from django.shortcuts import render

def index(request):
    from .forms import LogForm
    if (request.method=='POST'):

        form=LogForm(request.POST)

        if form.isvalid():
            pass

    else:
        form=LogForm()
    return render(request,'RecordEvent/Record.html')

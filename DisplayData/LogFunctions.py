import datetime
import json
from DisplayData import models

def gettime(timeStr):
    """reutrns a datetime corresponding to an input string"""
    current=datetime.datetime.now()
    if timeStr=='Day':
        return current-datetime.timedelta(days=1)
    elif timeStr=='Week':
        return current - datetime.timedelta(days=7)
    elif timeStr == 'Month':
        return current - datetime.timedelta(days=30)
    elif timeStr == '6 Months':
        return current - datetime.timedelta(days=186)
    else:
        return current - datetime.timedelta(days=365)

def buildHTML(measurable,theDate):
    """Build the log HTML on the server backend for security"""
    rows=models.Entries.objects.all().filter(parent=measurable).filter(timestamp__gte=theDate)
    buffer=''
    for row in rows:
        data=json.loads(row.data)
        value=""
        if 'value' in data:
            value+=str(data['value'])
            
        buffer+='<div class="padded"> <div class="download-body"><div class="row inline" style="padding-bottom: 10px"><div class="col-lg-6"><p>Time:<span class="value">{}</span> </p></div>'.format(row.timestamp)
        buffer+='<div class="col-lg-6"><p>Value: <span class="value">{}</span></p></div></div><p class="log">{}</p></div></div>'.format(value,data['log'])
    return buffer
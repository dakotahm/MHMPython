from django import forms
from RecordEvent import models
import json
from datetime import datetime


class LogForm(forms.Form):
    valueText=forms.IntegerField()
    tagText = forms.CharField(100)
    locationText = forms.CharField(100)
    DatePicker = forms.CharField(100)
    TimePicker = forms.CharField(100)


class ValidateRecordEvent():
    def __init__(self,dateInput,timeInput,log,value,measureId,userid,location):
         self.__dateInput=dateInput
         self.__timeInput=timeInput
         self.__log=log
         self.__value=value
         self.__measureId=measureId
         self.__userid = userid
         self.__location=location

    @property
    def jsonInput(self):
        try:
            dict={'log':self.__log,'value':int(self.__value),'location':self.__location}
            return json.dumps(dict)
        except ValueError:
            return None

    @property
    def theDate(self):
        try:
            datelist=[int(date) for date in self.__dateInput.split('/')]
            timelist=[int(time) for time in self.__timeInput.split(':')]
            datelist.extend(timelist)
            print(datelist)
            print(timelist)

            return datetime(datelist[2],datelist[0],datelist[1],datelist[3],datelist[4])
        except ValueError:
            print("Value is out of bounds")
            return None
        except IndexError:
            print("Index out of bounds")
            return None
    @property
    def ValidateAndSave(self):
        result=[self.jsonInput,self.theDate]
        if None in result:
            return False
        else:
            newRow=models.Entries(parent=self.__measureId,data=result[0],timestamp=result[1])
            newRow.save()
            return True


class ValidateNewLog():
    def __init__(self,name,maxVal,minVal,userId,type):
        self.__name=name
        self.__max=maxVal
        self.__min=minVal
        self.__userId=userId
        self.__type=type

    @property
    def name(self):
        if not self.__name.isspace():
            return self.__name
        else:
            return None

    @property
    def validateMaxMin(self):
        try:
            maxVal=int(self.__max)
            minVal=int(self.__min)
            assert(maxVal>minVal)
        except ValueError:
            return False
        except AssertionError:
            return False
        return True

    @property
    def ValidateAndAddMeasurable(self):
        if self.name!=None and self.validateMaxMin:
            newRow=models.Measurables(user_id=self.__userId,name=self.__name,max=self.__max,min=self.__min,type=self.__type)
            newRow.save()
            return True
        else:
            return False




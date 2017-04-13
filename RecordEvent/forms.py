from django import forms

class LogForm(forms.Form):
    valueText=forms.IntegerField()
    tagText = forms.CharField(100)
    locationText = forms.CharField(100)
    DatePicker = forms.CharField(100)
    TimePicker = forms.CharField(100)

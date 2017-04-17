from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from chartit import DataPool, Chart


def DisplayView(request):
    return render(request,'DisplayData/Display.html')


def get_data(request, *args, **kwargs):
	data = {
		"sales": 100,
		"customers": 10,
	}
	return JsonResponse(data)

class ChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		data = {
			"sales": 100,
			"customers": 10,
		}	
		return Response(data)

def weather_chart_view(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': Measurables.objects.all()},
              'terms': [
                'name',
                'type',
                'max',
                'min']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'name',
                    'type',
                    'max',
                    'min']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Weather Data of Boston and Houston'},
               'xAxis': {
                    'title': {
                       'text': 'Month number'}}})

    #Step 3: Send the chart object to the template.
    return render_to_response({'weatherchart': cht})






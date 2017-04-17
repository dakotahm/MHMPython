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
		labels = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
		default_items = [12, 11, 17, 12, 12, 2]
		data = {
			"labels": labels,
			"default": default_items,
		}	
		return Response(data)




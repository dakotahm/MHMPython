from django.shortcuts import render
from django.http import JsonResponse
from DisplayData import models

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

from chartit import DataPool, Chart


@login_required
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
		all_entries = models.Entries.objects.all()
		all_id = models.Entries.objects.all().values_list('id', flat=True)
		all_measurables = models.Measurables.objects.all().filter(user_id=request.user.id)
		all_parent = models.Entries.objects.all().values_list('parent', flat=True)
		labels = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
		default_items = [12, 11, 17, 12, 12, 2]
		data = {
			"labels": all_measurables,
			#"labels": all_id,
			#"default": all_parent,
		}	
		return Response(data)





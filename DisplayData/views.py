from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User


class AnalyticsIndexView(TemplateView):
    template_name = 'analytics/admin/index.html'

    def get_context_data(self, **kwargs):
        context = super(AnalyticsIndexView, self).get_context_data(**kwargs)
        context['30_day_registrations'] = self.thirty_day_registrations()
        return context

    def thirty_day_registrations(self):
        final_data = []

        date = arrow.now()
        for day in xrange(1, 30):
            date = date.replace(days=-1)
            count = User.objects.filter(
                date_joined__gte=date.floor('day').datetime,
                date_joined__lte=date.ceil('day').datetime).count()
            final_data.append(count)

        return final_data

def DisplayView(request):
    return render(request,'DisplayData/Display.html')


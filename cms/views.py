from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render
from events.models import EventModel
class HomeView(TemplateView):
    template_name='home.html'
    categories = EventModel.EVENT_CATEGORIES
    latest_events_list = EventModel.objects.order_by('-pk')[:4]
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'EventModel': EventModel.objects, 'categories':self.categories, 'latest_events_list':self.latest_events_list})

from .forms import EventCreationForm, EventSubUnsubForm
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render
from .models import EventModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django import forms
from django.views import View
from django.http import HttpResponseRedirect
class EventCreateView(LoginRequiredMixin, CreateView):
    login_url='/login/'
    template_name = 'event/create.html'
    form_class = EventCreationForm
    success_url = '/'
    pk = 0
    def get(self, request, *args, **kwargs):
        self.object = None
        context = self.get_context_data(**kwargs)
        global pk
        pk = self.kwargs['pk']
        
        return self.render_to_response(context)

    def form_valid(self, form):
        self.request.user.organizationmodel_set.get(pk = pk).eventmodel_set.create(event_name = form.cleaned_data.get('event_name'), event_date = form.cleaned_data.get('event_date'), event_photo = form.cleaned_data.get('event_photo'), event_category = form.cleaned_data.get('event_category'), event_detail = form.cleaned_data.get('event_detail'), event_addresses = form.cleaned_data.get('event_addresses'))
        return redirect('home')

class EventDetailView(TemplateView):
    template_name = 'event/detail.html'
    
    def get(self, request, *args, **kwargs):
        isParticipant = 1
        try:
            request.user.eventmodel_set.get(pk=self.kwargs['pk'])
        except:
            isParticipant = 0
        event = EventModel.objects.get(pk = self.kwargs['pk'])
        return render(request, self.template_name, {'event': event, 'isParticipant': isParticipant})
    def post(self, request, *args, **kwargs):
        try:
            request.user.eventmodel_set.get(pk=self.kwargs['pk'])
            event = EventModel.objects.get(pk = self.kwargs['pk'])
            event.event_participants.remove(request.user)
        except:
            event = EventModel.objects.get(pk = self.kwargs['pk'])
            event.event_participants.add(request.user)
        return HttpResponseRedirect(self.request.path_info)
class CategoryView(TemplateView):
    template_name = 'event/categories.html'
    EVENT_CHOICES = EventModel.EVENT_CATEGORIES
    def get(self, request, *args, **kwargs):
        found = 0
        for i in self.EVENT_CHOICES:
            if self.kwargs['category'] == i[0]:
                found = 1
                break
        if found == 1:
            events = EventModel.objects.filter(event_category = i[0])
            return render(request, self.template_name, {'events':events})
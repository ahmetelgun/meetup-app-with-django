from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render
from .models import OrganizationModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect



class OrganizationCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'organization/create.html'
    model = OrganizationModel
    fields = ['organization_name', 'organization_detail']
    success_url = '/'

    def form_valid(self, form):
        self.request.user.organizationmodel_set.create(organization_name = form.cleaned_data.get('organization_name'), organization_detail=form.cleaned_data.get('organization_detail'))
        return redirect('home')

class OrganizationDetailView(TemplateView):
    template_name = 'organization/detail.html'
    
    def get(self, request, *args, **kwargs):
        isMember=1
        try:
            request.user.members.get(pk = self.kwargs['pk'])
        except:
            isMember = 0
        organization = OrganizationModel.objects.get(pk = self.kwargs['pk'])
        latest_events_list = organization.eventmodel_set.order_by('-pk')[:3]
        latest_member_list = organization.organization_members.order_by('-pk')[:3]

        if len(OrganizationModel.objects.get(pk = self.kwargs['pk']).organization_members.all()) < 20:
            isCreateEvent = False
        else:
            isCreateEvent = True
        return render(request, self.template_name, {'organization': organization, 'latest_events_list':latest_events_list, 'isMember':isMember, 'isCreateEvent':isCreateEvent, 'latest_member_list':latest_member_list})
    
    def post(self, request, *args, **kwargs):
        try:
            request.user.members.get(pk = self.kwargs['pk'])
            organization = OrganizationModel.objects.get(pk = self.kwargs['pk'])
            organization.organization_members.remove(request.user)
        except:
            organization = OrganizationModel.objects.get(pk = self.kwargs['pk'])
            organization.organization_members.add(request.user)
        return HttpResponseRedirect(self.request.path_info)

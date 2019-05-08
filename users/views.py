from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views
from .forms import CustomUserCreationForm
from organizations.models import OrganizationModel
from .models import CustomUser
from django.views import View
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'signup.html'

class LoginView(views.LoginView):
    template_name = 'user/login.html'
    
class UserDetailView(View):
    template_name = 'user/detail.html'
    def get(self, request, *args, **kwargs):
        username = CustomUser.objects.get(username = self.kwargs['username'])
        return render(request, self.template_name, {'username': username})
    
class ProfileView(LoginRequiredMixin, View):
    login_url='/login/'
    template_name = 'user/account.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
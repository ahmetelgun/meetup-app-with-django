from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'users'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    
    path('user/<username>', views.UserDetailView.as_view(), name = 'detail'),
    path('account/', views.ProfileView.as_view(), name='account'),
]
from django.urls import path
from .views import OrganizationCreateView, OrganizationDetailView
app_name = 'organizations'
urlpatterns = [
    path('create/', OrganizationCreateView.as_view(), name='create'),
    path('organization_id/<int:pk>/', OrganizationDetailView.as_view(), name='detail'),
]
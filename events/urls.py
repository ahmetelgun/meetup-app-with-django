from django.urls import path
from .views import EventCreateView, EventDetailView, CategoryView
app_name = 'events'
urlpatterns = [
    path('<int:pk>', EventDetailView.as_view(), name='detail'),
    path('create/<int:pk>', EventCreateView.as_view(), name='create'),
    path('category/<slug:category>', CategoryView.as_view(), name='category'),
]

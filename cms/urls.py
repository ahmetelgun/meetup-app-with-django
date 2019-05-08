from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from users.views import LoginView
from django.conf.urls.static import static # new
from django.conf import settings # new
from events.models import EventModel
from .views import HomeView
urlpatterns = [
    path('', include('users.urls')),
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('organization/', include('organizations.urls')),
    path('event/', include('events.urls')),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

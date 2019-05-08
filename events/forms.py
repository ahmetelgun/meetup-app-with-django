from django import forms
from .models import EventModel
class DateInput(forms.DateInput):
    input_type = 'date'

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ['event_name', 'event_date', 'event_photo', 'event_category', 'event_detail', 'event_addresses']
        widgets = {
            'event_date': DateInput()
        }

class EventSubUnsubForm(forms.Form):
    pass
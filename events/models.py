from django.db import models
from organizations.models import OrganizationModel
from datetime import datetime
from users.models import CustomUser


class EventModel(models.Model):

    EVENT_CATEGORIES = (
        ('COM', "Bilgisayar"),
        ('LRN', "Öğrenme"),
        ('ART', "Sanat"),
        ('BK', "Kitap"),
        ('SCI', "Bilim"),
        ('FOD', "Yeme-İçme"),
        ('TRA', "Spor"),
        ('TCH', "Teknoloji")

    )
    event_name = models.CharField(max_length=30)
    event_date = models.DateField()
    event_photo = models.ImageField(upload_to='images/')
    event_participants = models.ManyToManyField(CustomUser)
    event_category = models.CharField(choices=EVENT_CATEGORIES, max_length=30, default='COM')
    organization = models.ForeignKey(OrganizationModel, on_delete=models.CASCADE)
    event_detail = models.TextField(max_length=2000)
    event_addresses = models.CharField(max_length=30)

    def __str__(self):
        return self.event_name

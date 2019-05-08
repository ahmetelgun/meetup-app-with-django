from django.db import models
from users.models import CustomUser
# Create your models here.

class OrganizationModel(models.Model):
    organization_name = models.CharField(max_length=30)
    organization_detail = models.TextField(max_length=2000)
    organization_members = models.ManyToManyField(CustomUser, related_name="members")
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="organizationmodel_set")

    def __str__(self):
        return self.organization_name
    


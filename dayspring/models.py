from django.db import models
from localflavor.us.models import PhoneNumberField, USStateField

class Member(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=75)
    phone = models.PhoneNumberField()
    address = models.CharField(max_length=255)
    state = models.USStateField()
    birth_month = models.PositiveIntegerField(null=True, blank=True)
    birth_day = models.PositiveIntegerField(null=True, blank=True)
    
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
    
    
from django.db import models
from localflavor.us.models import USStateField

class Member(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=75)
    home_phone = models.CharField(max_length=12)
    cell_phone = models.CharField(max_length=12)
    address = models.CharField(max_length=255)
    state = models.USStateField()
    birth_month = models.PositiveIntegerField(null=True, blank=True)
    birth_day = models.PositiveIntegerField(null=True, blank=True)
    
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
    
    
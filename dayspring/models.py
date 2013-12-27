from django.db import models
from localflavor.us.models import USStateField, PhoneNumberField
from swingtime import models as swingtime
import calendar
import datetime
import swingtime_settings

MONTH_CHOICES = tuple((m, m) for m in calendar.month_abbr[1:])
PART_CHOICES = (
    (u'S', u'Soprano'),
    (u'A', u'Alto'),
    (u'T', u'Tenor'),
    (u'B', u'Bass')
)

class Member(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=75)
    part = models.CharField(max_length=1, choices=PART_CHOICES, null=True, blank=True)
    email = models.EmailField(max_length=75, null=True, blank=True)
    home_phone = PhoneNumberField(null=True, blank=True)
    work_phone = PhoneNumberField(null=True, blank=True)
    cell_phone = PhoneNumberField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    birth_month = models.CharField(max_length=6, choices=MONTH_CHOICES, null=True, blank=True)
    birth_day = models.PositiveIntegerField(null=True, blank=True)
    
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
    
    def day_of_birth(self):
        return "%s %s" % (self.birth_month, self.birth_day)
    
class Piece(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=75)
    audio_version_url = models.URLField(null=True, blank=True)
    youtube_version_url = models.URLField(null=True, blank=True)
    soloists = models.ManyToManyField(Member, null=True, blank=True)

    def __unicode__(self):
        return self.title
    
    def display_soloists(self):
        return ", ".join([x.name for x in self.soloists.all()])

class Attendance(models.Model):
    occurrence = models.ForeignKey(swingtime.Occurrence)
    absences = models.ManyToManyField(Member, null=True, blank=True)
    pieces = models.ManyToManyField(Piece, null=True, blank=True)
    
    def __unicode__(self):
        return "%s on %s" % (self.occurrence.title, self.occurrence.start_time.strftime("%B %d, %Y"))
    
    def all_absences(self):
        return ", ".join([x.__unicode__() for x in self.absences.all()])
    
    def absences_count(self):
        return len(self.absences.all())
    
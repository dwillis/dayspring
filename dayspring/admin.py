from django.contrib import admin
from dayspring.models import Member, Piece, Attendance
from swingtime import models as swingtime

class MemberAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name","last_name")}
    search_fields = ['last_name']
    list_display = ('__unicode__', 'email', 'home_phone', 'cell_phone', 'work_phone', 'day_of_birth')
    list_filter = ('birth_month', 'part')
    ordering = ('last_name','first_name')

class PieceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title']
    list_display = ('title', 'audio_version_url', 'youtube_version_url', 'display_soloists')
    ordering = ('title',)

class AttendanceAdmin(admin.ModelAdmin):
    list_filter = ('occurrence',)
    list_display = ('__unicode__', 'all_absences')

def occurrence_unicode(self):
    return u'%s: %s' % (self.title, self.start_time.strftime("%b %d, %Y"))

swingtime.Occurrence.__unicode__ = occurrence_unicode

admin.site.register(swingtime.Occurrence)
admin.site.register(Member, MemberAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Attendance, AttendanceAdmin)

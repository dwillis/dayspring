from django.contrib import admin
from dayspring.models import Member, Piece, Event

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

class EventAdmin(admin.ModelAdmin):
    list_filter = ('event_type',)
    list_display = ('date', 'time', 'event_type', 'report_time', 'absences_count')
    ordering = ('-date', 'time')
    
admin.site.register(Member, MemberAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Event, EventAdmin)
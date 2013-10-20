from django.contrib import admin
from dayspring.models import Member

class MemberAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name","last_name")}
    search_fields = ['last_name']
    list_display = ('__unicode__', 'email', 'home_phone', 'cell_phone', 'work_phone', 'day_of_birth')
    list_filter = ('birth_month', 'part')
    ordering = ('last_name','first_name')
    
admin.site.register(Member, MemberAdmin)
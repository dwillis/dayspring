from django.contrib import admin
from dayspring.models import Member

class MemberAdmin(admin.ModelAdmin):
    search_fields = ['last_name']
    list_display = ('__unicode__', 'email', 'home_phone', 'cell_phone', 'day_of_birth')
    list_filter = ('birth_month', 'state')
    
admin.site.register(Member, MemberAdmin)
from django.contrib import admin
from .models import Info, TeamMember, Subscriber
# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_time')

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'description')

admin.site.register(Info, InfoAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Subscriber)
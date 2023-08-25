from django.contrib import admin
from .models import  Skill, Role, Venue, WalkIn
# Register your models here.

admin.site.register(Skill)
admin.site.register(Role)
admin.site.register(Venue)
admin.site.register(WalkIn)
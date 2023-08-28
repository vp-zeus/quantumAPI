from django.contrib import admin
from .models import Role, Venue, WalkIn, TimeSlot, Application
# Register your models here.

admin.site.register(Role)
admin.site.register(Venue)
admin.site.register(WalkIn)
admin.site.register(TimeSlot)
admin.site.register(Application)

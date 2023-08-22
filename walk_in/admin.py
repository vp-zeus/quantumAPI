from django.contrib import admin
from .models import  Degree, Stream, Skill, Role, College, Venue, WalkIn
# Register your models here.

admin.site.register(Degree)
admin.site.register(Stream)
admin.site.register(Skill)
admin.site.register(Role)
admin.site.register(College)
admin.site.register(Venue)
admin.site.register(WalkIn)
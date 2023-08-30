from ast import Try
from lib2to3.pytree import Base
from django.db import models


# Create your models here.

def file_upload_to(instance, filename):
    return 'files/{filename}'.format(filename=filename)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Role(BaseModel):
    name = models.CharField(max_length=45, blank=False)
    compensation = models.CharField(max_length=45)
    description = models.TextField()
    requirements = models.TextField()

    def __str__(self):
        return self.name


class Venue(BaseModel):
    name = models.TextField(blank=False)
    address_line_1 = models.TextField(blank=False)
    address_line_2 = models.TextField()
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    pincode = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    slot_start_time = models.TimeField()
    slot_end_time = models.TimeField()

    def __str__(self):
        return "{start_time} - {end_time}".format(start_time=self.slot_start_time.strftime("%H:%M:%S"), end_time=self.slot_end_time.strftime("%H:%M:%S"))


class WalkIn(BaseModel):
    name = models.TextField(blank=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    application_last_date = models.DateTimeField()
    general_instructions = models.TextField()
    instructions = models.TextField()
    min_sys_requirements = models.TextField()
    venue = models.ForeignKey(
        Venue, on_delete=models.CASCADE, related_name='walk_ins')
    roles = models.ManyToManyField(Role, related_name='walk_ins')
    available_time_slots = models.ManyToManyField(
        TimeSlot, related_name="walk_ins")

    def __str__(self):
        return self.name


class Application(BaseModel):
    profile = models.ForeignKey(
        "users.Profile", on_delete=models.CASCADE, related_name="applications", null=True)
    walk_in = models.ForeignKey(
        WalkIn, on_delete=models.CASCADE, related_name="applications")
    preferred_time_slot = models.ForeignKey(
        TimeSlot, on_delete=models.CASCADE, related_name="applications")

    preferred_roles = models.ManyToManyField(
        Role, related_name="applications", blank=True, null=True)

    applicant_resume = models.FileField(
        upload_to=file_upload_to, blank=True, null=True)

    def __str__(self):
        return self.profile.first_name

from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Skill(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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
    slot = models.TimeField()


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

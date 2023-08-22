from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Degree(BaseModel):
    name = models.CharField(max_length=100)

class Stream(BaseModel):
    name = models.CharField(max_length=100)

class Skill(BaseModel):
    name = models.CharField(max_length=100)

class Role(BaseModel):
    name = models.CharField(max_length=45,blank=False)
    compensation = models.CharField(max_length=45)
    description = models.TextField()
    requirements = models.TextField()

class College(BaseModel):
    name = models.TextField(blank=False)
    address_line_1 = models.TextField(blank=False)
    address_line_2 = models.TextField()
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    pincode = models.CharField(max_length=45)
    

class Venue(BaseModel):
    name = models.TextField(blank=False)
    address_line_1 = models.TextField(blank=False)
    address_line_2 = models.TextField()
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    pincode = models.CharField(max_length=45)

class User(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=500)

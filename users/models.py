from lib2to3.pytree import Base
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from walk_in.models import Role, BaseModel
from .managers import CustomUserManager


class User(AbstractUser, BaseModel):
    class Meta:
        db_table = 'auth_user'
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    phone = models.CharField(max_length=20)
    portfolio_URL = models.TextField(blank=True)
    preferred_roles = models.ManyToManyField(Role, related_name='users')
    referral = models.TextField(blank=True)
    mail_list = models.BooleanField(blank=True)


class Degree(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Stream(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class College(BaseModel):
    name = models.TextField(blank=False)
    address_line_1 = models.TextField(blank=False)
    address_line_2 = models.TextField()
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    pincode = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class EducationalQualification(BaseModel):
    aggregate_percentage = models.SmallIntegerField()
    year_of_passing = models.CharField(max_length=4)
    degree = models.ForeignKey(
        Degree, on_delete=models.CASCADE, related_name="educational_qualifications")
    stream = models.ForeignKey(
        Stream, on_delete=models.CASCADE, related_name="educational_qualifications")
    college = models.ForeignKey(
        College, on_delete=models.CASCADE, related_name="educational_qualifications")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="educational_qualifications")

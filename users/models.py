from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from walk_in.models import Role, BaseModel
from .managers import CustomUserManager


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


def file_upload_to(instance, filename):
    return 'files/{filename}'.format(filename=filename)


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
    portfolio_url = models.TextField(blank=True)
    preferred_roles = models.ManyToManyField(Role, related_name='users')
    referral = models.TextField(blank=True)
    mail_list = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to=upload_to, null=True)
    resume = models.FileField(upload_to=file_upload_to, null=True)

    def __str__(self):
        return self.first_name


class Degree(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Stream(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Skill(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class College(BaseModel):
    name = models.TextField()
    address_line_1 = models.TextField()
    address_line_2 = models.TextField(blank=True)
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
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="educational_qualification")


class ProfessionalQualification(BaseModel):
    applicant_type = models.CharField(max_length=45)
    experience = models.IntegerField(null=True, blank=True)
    current_ctc = models.CharField(blank=True, max_length=45)
    expected_ctc = models.CharField(blank=True, max_length=45)
    other_skills = models.TextField(blank=True)
    on_notice_period = models.BooleanField(default=False)
    notice_period_end = models.DateField(blank=True, null=True)
    notice_period_duration = models.IntegerField(null=True, blank=True)
    applied_recently = models.BooleanField()
    applied_role = models.TextField(blank=True)
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="professional_qualification")
    expert_skills = models.ManyToManyField(
        Skill, related_name="expert_skills")
    familiar_skills = models.ManyToManyField(
        Skill, related_name="familiar_skills")

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from walk_in.models import Role,BaseModel
from .managers import CustomUserManager

class User(AbstractUser,BaseModel):
    class Meta:
        db_table = 'auth_user'
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Profile(BaseModel):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    phone = models.CharField(max_length=20)
    portfolio_URL = models.TextField(blank=True)
    preferred_roles = models.ManyToManyField(Role,related_name='users')
    referral = models.TextField(blank=True)
    mail_list = models.BooleanField(blank=True)
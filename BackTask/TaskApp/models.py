from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.html import mark_safe

# Create your models here.


GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
)


class Address(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=6)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country


class Profile(AbstractUser):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile/', null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    permanent_address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, blank=True,
                                             related_name='user_permanent_address')
    company_address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, blank=True,
                                           related_name='user_company_address')
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_friends', blank=True)

    def save(self, *args, **kwargs):
        self.name = '{0} {1}'.format(self.first_name, self.last_name)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.phone_number

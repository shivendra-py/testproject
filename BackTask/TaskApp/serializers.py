from rest_framework import serializers
from TaskApp.models import *


class registrationserializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('name','email','phone_number','gender','profile_pic','date_of_birth','company_address','permanent_address','friends')
    
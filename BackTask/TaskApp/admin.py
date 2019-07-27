from django.contrib import admin
from TaskApp import models
from django.utils.html import format_html

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'profile_image')
    search_fields = ('first_name', 'last_name', 'name')
    list_filter = ('gender', 'permanent_address__city', 'company_address__city')

    @staticmethod
    def profile_image(obj):
        img_url = "https://res.cloudinary.com/null-null/image/upload/v1563774150/learner_eo2pl4.png"
        if obj.profile_pic.name != "":
            img_url = obj.profile_pic.url
        return format_html('<img src="{}" width="42" height="42">'.format(img_url))


admin.site.register(models.Profile, ProfileAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ['street_address', 'city', 'state', 'pin_code', 'country']
    search_fields = ['city', 'state', 'pin_code', 'country']
    list_filter = ('city', 'state', 'pin_code', 'country')


admin.site.register(models.Address, AddressAdmin)

from django.contrib import admin
from django.contrib.auth.models import User
from . import models

admin.site.register(models.Category)
admin.site.register(models.Customer)
admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.Profile)


class ProfileAdmin(admin.StackedInline):
    model = models.Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    verbose_name = 'profile'


class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = (ProfileAdmin,)
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
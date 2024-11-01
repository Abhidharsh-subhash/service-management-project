from django.contrib import admin
from . import models
from django.contrib.auth.models import Group, User

# Register your models here.


admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(models.Users)
class Users(admin.ModelAdmin):
    list_display = ("username", "email", "updated_at")
    exclude = ("password",)


admin.site.register(models.category)
admin.site.register(models.Staffs)
from django.contrib import admin
from userauths.models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = [ 'username', 'email','bio']
    



admin.site.register(User, UserAdmin)


# @admin.register()

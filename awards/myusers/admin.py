from django.contrib import admin

from myusers.models import Profile
from .models import Profile

# Register your models here.
admin.site.register(Profile)


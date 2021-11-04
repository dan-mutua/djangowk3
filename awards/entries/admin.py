from django.contrib import admin
from .models import Entry,UserProfile,Comment

# Register your models here.
admin.site.register(Entry)
admin.site.register(UserProfile)
admin.site.register(Comment)

from django.contrib import admin
from .models import Entry,Profile,Comment

# Register your models here.
admin.site.register(Entry)
admin.site.register(Profile)
admin.site.register(Comment)

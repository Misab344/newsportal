from django.contrib import admin

# Register your models here.
from .models import Profile, Interest, Message

admin.site.register(Profile)
admin.site.register(Interest)
admin.site.register(Message)


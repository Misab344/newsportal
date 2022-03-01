from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    short_intro = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    profile_image = models.ImageField(default='profile/user-default.png', upload_to='profile/', null=True, blank=True)
    interest_category = models.ManyToManyField('Interest', blank=True, related_name='interest')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

    @property
    def profileURL(self):
        try:
            img = self.profile_image.url
        except:
            img = ''
        return img


class Interest(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)
import uuid

from django.db import models
from newsportal.user.models import Profile


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


# Create your models here.
class News(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(
        default='images/cat.jpg', null=True, blank=True
    )
    image_link = models.CharField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            img = self.featured_image.url

        except:
            img = ''
        return img


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(News, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.value


class TopNews(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    top = models.ForeignKey(News, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.top.title




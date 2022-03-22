import uuid

from django.db import models
from user.models import Profile


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
        default='news/default.jpg', null=True, blank=True, upload_to='news/'
    )
    image_link = models.CharField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    verified_news = models.BooleanField(blank=True, null=True)

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
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.body


class TopNews(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    top = models.ForeignKey(News, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.top.title



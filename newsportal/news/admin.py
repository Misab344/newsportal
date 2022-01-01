from django.contrib import admin


from .models import News, Category, TopNews, Review

# Register your models here.

admin.site.register(News)
admin.site.register(Category)
admin.site.register(TopNews)
admin.site.register(Review)

from django.db.models.base import Model
from django.forms import ModelForm, widgets


from django import forms
from .models import News, Review


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = [
            'title', 'category', 'description', 'featured_image', 'image_link'
        ]

        def __init__(self, *args, **kwargs):
            super(NewsForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['body']

        labels = {
            'body': 'Add a comment'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

from django import forms
from django.forms import ModelForm

from .models import News, Person, Comment


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['post_name', 'post_description', 'post_img', 'popular']


class UserForm(ModelForm):
    class Meta:
        model = Person
        fields = ['email', 'password']


class CommentForm(ModelForm):
    class Meta:
        model= Comment
        fields = ['Comment', 'like']


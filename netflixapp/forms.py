from django import forms
from .models import Netflix, Comment

class netflixForm(forms.ModelForm):
    class Meta:
        model = Netflix
        fields = ['title','director', 'genre', 'score', 'content', 'img']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']
from django import forms
from .models import Netflix

class netflixForm(forms.ModelForm):
    class Meta:
        model = Netflix
        fields = ['title','director', 'genre', 'score', 'content', 'img']
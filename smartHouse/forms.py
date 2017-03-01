from django import forms
from .models import room

class PostForm(forms.ModelForm):

    class Meta:
        model = room
        fields = ('state', )
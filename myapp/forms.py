from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your tweet here...'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

class   UserCreationForm(UserCreationForm): 
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
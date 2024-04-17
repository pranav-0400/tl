from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    commenter = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'Your name'
    }))
    body = forms.CharField(max_length=100, widget = forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'Comment here', 'rows': 3
    }))
    class Meta:
        model = Comment
        fields = ['commenter', 'body']
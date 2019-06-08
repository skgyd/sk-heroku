from django import forms
from .models import Comment
from .models import Blog

class CommentForm(forms.ModelForm):
    class Meta: 
        model=Comment
        fields=('author','text',)

class BlogPost(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title','body',)


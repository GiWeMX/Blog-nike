from django import forms
from .models import Post, Comment

from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'description', 'category']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputTitle'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'inputImage'
            }),
            'description': SummernoteWidget(),
            'category': forms.CheckboxSelectMultiple()
        }



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']

    text = forms.CharField(max_length=300) 
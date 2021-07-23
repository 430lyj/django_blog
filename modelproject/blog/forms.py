from django import forms
from django.forms import fields
from .models import Blog
from .models import Comment

class BlogForm(forms.ModelForm):
    title = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={ 'class': 'title-inputs',
                                        'placeholder': 'Title'})
        )
    body = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={ 'class': 'body-inputs',
                                        'placeholder': '공유하고 싶은 일상을 적어보세요.'})
        )

    class Meta:
        model = Blog
        fields = ['title', 'body', 'image']
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'class':"form-control",
                    'id':"BlogformFile"
                }
            )
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
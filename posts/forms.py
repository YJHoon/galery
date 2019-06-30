from django import forms
from .models import Post
from .models import Post, Comment, Galery

class GaleryForm(forms.ModelForm):
    class Meta:
        model = Galery
        fields = [
            'title'
        ]
        labels = {
            'title': "제목"
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content'
        ]
        labels = {
            'title': "제목",
            'content': "내용"
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]
        labels = {
            'content': "내용",
        }

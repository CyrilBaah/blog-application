from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    """Email Form Template"""
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)
    

class CommentForm(forms.ModelForm):
    # Form representing a comment
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        
        
class SearchForm(forms.Form):
    # Form representing a search
    query = forms.CharField()
    
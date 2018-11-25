from django import forms
from .models import Comment
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):  #We used ModelForm(because we have to build a form dynamically for our 'Comment' model)to let our users comment on blog post.
    class Meta:
        model = Comment
        fields = ('name','email','body')


class SearchForm(forms.Form):
    query = forms.CharField()
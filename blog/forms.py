from django import forms

from .models import CommentModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ["blog"]
        labels = {
            "commentor_name":"Name",
            "commentor_email":"Email",
            "comment_text":"Comment"
        }
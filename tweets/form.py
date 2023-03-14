from django import forms

from .models import Tweet

MAX_TWEET_LENGTH = 240

class TweetForm(forms.ModelForm):
    class Meta: #Meta class is describing the whole form itself
        # content = forms.CharField() #character field
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("This tweet is too long")
        return content

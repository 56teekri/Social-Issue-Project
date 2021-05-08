from django import forms
from main import models

class SocialIssueForm(forms.ModelForm):
    class Meta:
        model=models.SocialIssue
        fields=["title","description"]


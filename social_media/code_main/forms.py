from django import  forms
from code_main.models import post

class postfrom(forms.ModelForm):
    class Meta:
        model=post
        fields=['image','caption']


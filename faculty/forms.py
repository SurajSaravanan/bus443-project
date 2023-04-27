from django.forms import ModelForm, TextInput, EmailInput
from faculty.models import Facultycomment

class CommentForm(ModelForm):
    class Meta:
        model = Facultycomment
        fields = ['facultyemail', 'facultycomment']
        widgets = {
            'facultyemail': EmailInput(attrs = {
                'class': 'form-control',
                'style': 'max-width:300px',
                'placeholder': 'Please enter your email id',
            }),
            'facultycomment': TextInput(attrs = {
                'class': 'form-control',
                'style': 'max_width: 500px',
                'placeholder': 'Please enter your comment',
            })
        }
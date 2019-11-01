from django import forms
from .models import Post


class ContactForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nome'}
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email'}
        )
    )
    msg = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Fale conosco'}
        )
    )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'text']


from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100,label='Your Name', label_suffix=' ')
    password = forms.CharField(widget=forms.PasswordInput, label_suffix=' ')
from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100,label='Your Name', label_suffix=' ', initial='Rabbi',help_text='Your name must less then 10 character')
    password = forms.IntegerField(widget=forms.PasswordInput(attrs={'class':'inputField'}), label_suffix=' ')
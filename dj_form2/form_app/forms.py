from django import forms

class NameForm(forms.Form):
    subject = forms.CharField(max_length=100,help_text='You can not write more then 30 character.')
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
from django import forms

def start_with_r(value):
    if value[0] != 'r':
        raise forms.ValidationError("Name must be start with R")


class StudentForm(forms.Form):
    name = forms.CharField(max_length=100,label='Your Name', label_suffix=' ', validators=[start_with_r])
    password = forms.CharField(widget=forms.PasswordInput, label_suffix=' ')

    # single field validation in Form
    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if len(name) < 4:
    #         raise forms.ValidationError('Your name must be greater then 4 character.')
    #     return name


    # multiple field validation in Form
    def clean(self):
        cleaned_data = super().clean()
        name = self.cleaned_data.get('name')
        password = self.cleaned_data.get('password')

        if len(name)<4:
            raise forms.ValidationError('Your name must be greater then or equal 4 characters.')
        
        if len(password)<8:
            raise forms.ValidationError('Your password must be greater then or equal 8 characters.')
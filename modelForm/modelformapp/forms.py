from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
        labels = {'name':'Enter your name', 'roll':'Enter your roll', 'city':'Enter your city'}

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'Rakib':
            raise forms.ValidationError('Rakib name is not allowed')
        return name
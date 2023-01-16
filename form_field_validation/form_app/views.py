from django.shortcuts import render
from .forms import StudentForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            password = fm.cleaned_data['password']
            print('Name : ', name)
            print('Password : ', password)

    else:
        fm = StudentForm()
    return render(request, 'form_app/index.html', {'form':fm})
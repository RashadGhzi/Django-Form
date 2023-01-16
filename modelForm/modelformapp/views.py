from django.shortcuts import render
from .models import Student
from .forms import StudentForm
# Create your views here.
def index(request):
    if request.method=='POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = StudentForm(label_suffix=' ')
    return render(request,'modelformapp/index.html', {'form':fm})
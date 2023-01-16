from django.shortcuts import render
from .forms import StudentForm
# Create your views here.
def index(request):
    fm = StudentForm()
    return render(request, 'form_app/index.html', {'form':fm})
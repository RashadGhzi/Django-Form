from django.shortcuts import render
from .forms import NameForm
# Create your views here.
def index(request):
    fm = NameForm(auto_id=True, label_suffix="--", initial={'subject':'Learn Form in django', 'sender':'Rabbi','cc_myself':True})
    # ordering fields
    fm.order_fields(field_order=['message','sender','subject','cc_myself'])
    return render(request, 'form_app/index.html', {'form':fm})
from django.shortcuts import render,redirect, HttpResponse

# Create your views here.
from .models import  CoverLetter
from .forms import CoverLetterForm
def index(request):
    return render(request,'index.html')

def create_cover(request):
    if request.method == 'POST':
        form = CoverLetterForm(request.POST)
        if form.is_valid():
            cover = form.save()
            return redirect('index')
        else:
            return HttpResponse('form is not valid')
    else:
        form = CoverLetterForm()
        context = {'form':form}
        return render(request,"coverit/cover_create.html", context)

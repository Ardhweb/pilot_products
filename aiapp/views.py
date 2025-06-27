from django.shortcuts import render

# Create your views here.
from aiapp.models import UploadAnalyzedFile
from aiapp.forms import  UploadeFileForm



def analyzer_upload(request):
    form  = UploadeFileForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid ():
            form = form.save(commit=False)
            form.user = request.user
            form.original_filename = "Dmange"
            form.save()
            return redirect('home')
    else:
        form = UploadeFileForm()
    return render(request, 'aiapp/analyzer/upload_file.html', {'form':form})


def cover_draft(request):
    return render(request,"aiapp/cover/draft_chat.html")
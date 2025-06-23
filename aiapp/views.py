from django.shortcuts import render

# Create your views here.
from aiapp.models import UploadAnalyzedFile
from aiapp.forms import  UploadeFileForm



def analyzer_upload(request):
    form  = UploadeFileForm(POST)
    if request.method == 'POST':
        if form.is_valid():
            form = form.save(commit=False)
            
    return render(request, 'aiapp/analyzer/upload_file.html')
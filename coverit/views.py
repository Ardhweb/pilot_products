from django.shortcuts import render,redirect, HttpResponse

# Create your views here.
from .models import  CoverLetter
from .forms import CoverLetterForm
from django.shortcuts import redirect, reverse
from django.template.loader import get_template
from weasyprint import HTML
from django.views import View
from django.contrib.auth.decorators import login_required
import google.generativeai as genai
import os
from django.http import JsonResponse

from django.conf import settings 
# Load API Key
GENAI_API_KEY = settings.FLASH_AI_KEY  # Use environment variable for security
genai.configure(api_key=GENAI_API_KEY)
#client = genai.Client(api_key=GENAI_API_KEY)


def index(request):
    return render(request, 'coverit/index.html')

@login_required
def generate_text_view(request):
    if request.method == "GET":
        prompt = request.GET.get("prompt", "Hello AI!")
        max_chars = int(request.GET.get("max_chars", 200))  # Default to 200 characters
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)

            # Trim the response if it exceeds the limit
            trimmed_response = response.text[:max_chars]

            return JsonResponse({"response": trimmed_response})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@login_required
def create_cover(request):
    breadcrumbs = [
        {'name': 'Page 1', 'url': '/'},
        {'name': 'Page 2', 'url': '/about/'},
        {'name': 'Contact', 'url': None},  # Current page with no URL
    ]
    if request.method == 'POST':
        form = CoverLetterForm(request.POST)
        if form.is_valid():
            cover = form.save(commit=False)  # Create the instance but don't save yet
            cover.candidate = request.user if request.user.is_authenticated else None
            cover = form.save()
            id = cover.id
            title = cover.title
            print(id)
            # return redirect('index')
            # return redirect(reverse('generate_pdf', args=[id]))
            return redirect(reverse('cover_view', args=[id,title]))
        else:
            return HttpResponse('form is not valid')
    else:
        form = CoverLetterForm()
        breadcrumbs = [
        {'name': 'Page 1', 'url': '/'},
        {'name': 'Page 2', 'url': '/about/'},
        {'name': 'Contact', 'url': None},  # Current page with no URL
        ]

        context = {'form':form,'breadcrumbs': breadcrumbs,
        'page1':'Writeup', 'page2':'Gen', 'page3':'Thank you'}
        return render(request,"coverit/cover_create.html", context)

@login_required
def cover_th(request,title,id):
    cover_data = {
        'title':title,
        'id':id
    }
    downlload_cover = CoverLetter.objects.get(id=id)
    return render(request,'coverit/thank.html', {'cover_data':cover_data, 'downlload_cover':downlload_cover})


class PDFView(View):
    def get(self, request, id,*args, **kwargs):
        letter_id = id
        data = CoverLetter.objects.get(id=letter_id)
        template = get_template('coverit/weasy/pdf_template.html')  # Your HTML template
        html = template.render({'data':data})  # Pass any context variables
        pdf = HTML(string=html).write_pdf()

        # Check if 'download' is in the URL parameters
        is_download = request.GET.get('download', '0') == '1'

        response = HttpResponse(pdf, content_type='application/pdf')
        if is_download:
            response['Content-Disposition'] = 'attachment; filename="document.pdf"'
        else:
            response['Content-Disposition'] = 'inline; filename="document.pdf"'
        
        return response



@login_required
def indexing_cover_l(request):
    if request.user.is_authenticated:
        letter = CoverLetter.objects.filter(candidate_id=request.user.id)
        context = {'letter':letter}
        return render(request,'coverit/listing.html', context)
    else:
        return redirect('cover-home')
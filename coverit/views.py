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
import markdown
from django.conf import settings 
from .utils import  dynamic_spinner_script
# Load API Key
GENAI_API_KEY = settings.FLASH_AI_KEY  # Use environment variable for security
genai.configure(api_key=GENAI_API_KEY)
#client = genai.Client(api_key=GENAI_API_KEY)




# @login_required
# def generate_text_view(request):
#     if request.method == "GET":
#         prompt = request.GET.get("prompt", "Hello AI!")
#         max_chars = int(request.GET.get("max_chars", 200))  # Default to 200 characters
#         try:
#             model = genai.GenerativeModel("gemini-1.5-flash")
#             response = model.generate_content(prompt)

#             # Trim the response if it exceeds the limit
#             trimmed_response = response.text[:max_chars]

#             return JsonResponse({"response": trimmed_response})
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)


from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
import json
import google.generativeai as genai

@login_required
def generate_text_view(request):
    """ Securely generate text using Gemini Flash """

    # Only allow AJAX requests (prevents direct access)
    if not request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return HttpResponseForbidden("Access Denied")

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            prompt = data.get("prompt", "Hello AI!")
            max_chars = int(data.get("max_chars", 500))  # Default 200 chars

            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)

            # Trim response
            trimmed_response = response.text[:max_chars]

            return JsonResponse({"response": trimmed_response})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return HttpResponseForbidden("Invalid Request")





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

'''
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

'''
class PDFView(View):
    def get(self, request, id, *args, **kwargs):
        letter = CoverLetter.objects.get(id=id)
        letter_content_markdown = markdown.markdown(letter.contents)
        context = {
            'letter': letter,
            'name':request.user.get_full_name(),
            'email': request.user.email,
            "letter_content_markdown":letter_content_markdown,
            # pass as-is
        }

        template = get_template('coverit/weasy/pdf_template.html')
        html = template.render(context)
        pdf = HTML(string=html).write_pdf()

        is_download = request.GET.get('download', '0') == '1'
        response = HttpResponse(pdf, content_type='application/pdf')
        disposition = 'attachment' if is_download else 'inline'
        response['Content-Disposition'] = f'{disposition}; filename="document.pdf"'

        return response



@login_required
def indexing_cover_l(request):
    if request.user.is_authenticated:
        letters = CoverLetter.objects.filter(candidate_id=request.user.id)
        context = {'letters':letters}
        return render(request,'coverit/listing.html', context)
    else:
        return redirect('index')
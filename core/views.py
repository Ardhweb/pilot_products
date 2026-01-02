from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import subprocess
from .export import html_to_pdf, html_to_pdf_view
import weasyprint
from django.template.loader import render_to_string
from core.forms import BlankDesignForm
from django.contrib.auth.decorators import login_required
from core.models import LetterDesign
from uuid import UUID

@csrf_exempt
def github_webhook(request):
    if request.method == 'POST':
        repo_dir = '/home/pilotprojects/pilotproducts/'
        try:
            os.chdir(repo_dir)
            subprocess.run(['git', 'fetch', 'origin'], check=True)
            subprocess.run(['git', 'checkout', 'main'], check=True)
            subprocess.run(['git', 'pull', 'origin', 'main'], check=True)
            return JsonResponse({'status': 'success'}, status=200)
        except subprocess.CalledProcessError as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)





def homepage(request):
    # from sentence_transformers import SentenceTransformer

    # model = SentenceTransformer('all-MiniLM-L6-v2')  # Downloads model if needed
    # sentence = "This is a test sentence."
    # embedding = model.encode(sentence)
    
    # print("Embedding shape:", embedding.shape)

    return render(request, "core/index.html")



from django.shortcuts import render
from django.conf.urls import handler404

def error_404(request, exception):
    return render(request, 'error_pages/404.html', status=404)


def a4_letter(request):
    return render(request,'pages/a4_template.html')

@login_required
def test_page(request,l_id:UUID):
    context_content = None
    cu = get_object_or_404(LetterDesign, lc_id=l_id)
    if cu:
        return render(request, 'pages/tp-20251104-s4cU.html')
    else:
        print(f"No LetterDesign found for user {request.user} and id {lc_id}")
        return HttpResponse("Not Allowed couldn't find Letter")

from bs4 import BeautifulSoup

def view_page_pdf(request):
    input_html = 'pages/tp-20251104-s4cU.html'
    html_content = render_to_string(input_html) 
    soup = BeautifulSoup(html_content, 'html.parser')
    canvas_design = soup.find(id="canvas") 
    if canvas_design:
        head_content = soup.head
        body_content = soup.body

        # Create a new body content with only the canvas content
        new_body = soup.new_tag('body')
        new_body.append(canvas_design)  # Add canvas div to new body

        # Reconstruct the full HTML with head and new body content
        new_html = soup.new_tag('html')
        new_html.append(head_content)
        new_html.append(new_body)
        reconstructed_html = str(new_html)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=page_cover_letter'
    # weasyprint.HTML(string=html_content).write_pdf(response)
    weasyprint.HTML(string=reconstructed_html).write_pdf(response)
    return response

@login_required
def _blank_design_generate(request):
    
    if request.method == 'POST':
        form = BlankDesignForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            print(f"Saved D:{instance.lc_id}")
            return redirect('test_page', lc_id="6fc4ea3b0c554369822d9fe3f0a09759")
        else:
            print(form.errors)
            return HttpResponse("<h1>Hello from Django!</h1>")
    else:
        form = BlankDesignForm()
        
        return render(request,'forms/select_design.html',{'form':form})

@login_required
def my_letters(request):
    """ 
    This code is responsobile to  fetach each letter related current requested user 
    and then show to  my letters page of that related user all data.
    """
    cover_letters = LetterDesign.objects.filter(user=request.user)
    print(cover_letters)
    return render(request, "pages/my_letters.html", {'cover_letters':cover_letters})
    
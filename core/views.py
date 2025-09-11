from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import subprocess
from .export import html_to_pdf, html_to_pdf_view
import weasyprint
from django.template.loader import render_to_string

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

def test_page(request):
    context_content = None
    return render(request,'pages/testpage.html')

from bs4 import BeautifulSoup

def view_page_pdf(request):
    input_html = 'pages/testpage.html'
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
    

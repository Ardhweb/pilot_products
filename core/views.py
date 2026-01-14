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
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.conf.urls import handler404
import json
from weasyprint import HTML

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


def error_404(request, exception):
    return render(request, 'error_pages/404.html', status=404)

def a4_letter(request):
    return render(request,'pages/a4_template.html')

@login_required
def test_page(request,l_id:UUID):
    context_content = None
    cu = get_object_or_404(LetterDesign, lc_id=l_id)
    if cu:
        return render(request, 'pages/tp-20251104-s4cU.html', {"cu":cu})
    else:
        print(f"No LetterDesign found for user {request.user} and id {lc_id}")
        return HttpResponse("Not Allowed couldn't find Letter")
        
# @login_required
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



def view_page_pdf(request):
    # Step 1: Load the HTML template
    input_html = 'pages/tp-20251104-s4cU.html'
    html_content = render_to_string(input_html)

    # Step 2: Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Step 3: Extract only the canvas
    canvas_design = soup.find(id="canvas")
    if not canvas_design:
        return HttpResponse("Canvas not found!", status=404)

    # Step 4: Fetch state data from DB
    state_data = LetterDesign.objects.get(lc_id='9ee024ee-ee0c-455f-ac0b-b40bd057072d')
    updated_json_data = state_data.state_data

    # Ensure it's a dict
    if isinstance(updated_json_data, str):
        updated_data = json.loads(updated_json_data)
    else:
        updated_data = updated_json_data

    # Step 5: Update the canvas and child nodes in Python
    # Update canvas (root) properties
    root_geom = updated_data['c']['d']['g']
    canvas_design['style'] = f"""
        width: {root_geom['h']['i']}px;
        height: {root_geom['h']['j']}px;
        background-color: {root_geom['o']};
        position: relative;
    """

    # Update all nodes (TextLayer, ImageLayer, etc.)
    nodes = updated_data['nodes']
    root_children = updated_data['c']['d']['s']
    
    def process_node(node_key, parent_element):
        node = nodes.get(node_key)
        if not node:
            return
        
        element = soup.find(id=node_key)
        if not element:
            # Create element if missing
            if node['e']['f'] == 'ImageLayer':
                element = soup.new_tag('img', id=node_key)
            else:
                element = soup.new_tag('div', id=node_key)
                element['class'] = "section resizable"
            parent_element.append(element)

        # Apply geometry
        g = node['g']
        element['style'] = f"""
            position: absolute;
            left: {g['k']['l']}px;
            top: {g['k']['m']}px;
            width: {g['h']['i']}px;
            height: {g['h']['j']}px;
        """
        # Apply style
        if 'style' in node:
            s = node['style']
            if 'color' in s:
                element['style'] += f" color: {s['color']};"
            if 'fontSize' in s:
                element['style'] += f" font-size: {s['fontSize']}px;"
            if 'fill' in s:
                element['style'] += f" background-color: {s['fill']};"
            if 'stroke' in s:
                element['style'] += f" border: 1px solid {s['stroke']};"

        # Apply content
        if node['e']['f'] in ['TextLayer', 'RootLayer'] and 'content' in node:
            element.string = node['content']
            element['contenteditable'] = 'true'
        if node['e']['f'] == 'ImageLayer' and 'src' in node:
            element['src'] = node['src']

        # Recursively process children
        for child_key in node.get('s', []):
            process_node(child_key, element)

    # Process root-level children
    for node_key in root_children:
        process_node(node_key, canvas_design)

    # Step 6: Build a new body with only the canvas
    new_body = soup.new_tag('body')
    new_body.append(canvas_design)

    # Step 7: Reconstruct full HTML
    new_html = soup.new_tag('html')

    # Get the existing <style> tag from <head>
    head_content = soup.head
    style_tag = head_content.find('style')

    # Create a new <style> tag and copy the contents of the old one
    if style_tag:
        new_style_tag = soup.new_tag('style')
        new_style_tag.string = style_tag.string  # Copy the content of the old <style> tag

        # Append the new <style> tag to the new head
        new_html.append(new_style_tag)

    # Add the new body content (canvas)
    new_html.append(new_body)

    reconstructed_html = str(new_html)
    print(reconstructed_html)

    # Step 8: Generate PDF
    pdf = HTML(string=reconstructed_html).write_pdf()

    # Step 9: Return PDF as page (inline)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="page_cover_letter.pdf"'
    return response



@login_required
def my_letters(request):
    """ 
    This code is responsobile to  fetach each letter related current requested user 
    and then show to  my letters page of that related user all data.
    """
    cover_letters = LetterDesign.objects.filter(user=request.user)
    print(cover_letters)
    return render(request, "pages/my_letters.html", {'cover_letters':cover_letters})
    
from django.shortcuts import render,redirect, HttpResponse

# Create your views here.
from .models import  CoverLetter
from .forms import CoverLetterForm
from django.shortcuts import redirect, reverse
from django.template.loader import get_template
from weasyprint import HTML
from django.views import View


def index(request):
    return render(request, 'coverit/index.html')
    
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
            cover.candidate = request.user   
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


def cover_th(request,title,id):
    cover_data = {
        'title':title,
        'id':id
    }
    return render(request,'coverit/thank.html', {'cover_data':cover_data})

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


def indexing_cover_l(request):
    if request.user.is_authenticated:
        letter = CoverLetter.objects.all()
        print(letter)
        context = {'letter':letter}
        return render(request,'coverit/listing.html', context)
    else:
        return redirect('index')
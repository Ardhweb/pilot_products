from django.shortcuts import render,redirect

# Create your views here.
from .models import DailyParent, AnchorCheckPoint, ListItem
from .forms import CreateDailyForm
from django.urls import reverse
def create_parent(request):
    if request.method == "POST":
        form = CreateDailyForm(request.POST)
        if form.is_valid():
            instance = form.save()
            anchor = AnchorCheckPoint.objects.create(dailyparent=instance)
            print(anchor.id)
            url = reverse("timeline:item_add", kargs=[anchor.id])  # or kwargs={'id': user_id}
            return redirect(url)
    else:
        form = CreateDailyForm()
    return render(request, 'timeline/parent.html', {'form':form})

def parent_list(request):
    objs =  DailyParent.objects.all()
    context = {'objs':objs}
    return render(request,'timeline/list.html', context)

def add_item(request, id):
    anchor = get_object_or_404(AnchorCheckPoint, id)
    return render(request, 'timeline/add-item.html', {'anchor':anchor})


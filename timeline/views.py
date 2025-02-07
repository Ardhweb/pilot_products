from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from .models import DailyParent,AnchorCheckPoint, ListItem
from .forms import CreateDailyForm
from django.urls import reverse

def anchorpoint(request,id):
    anchor_obj = AnchorCheckPoint.objects.get(pk=id)
    print(anchor_obj)
    if request.method == "POST":
        tasks = request.POST.getlist("task")  # Get all task inputs with the same name
        for task_text in tasks:
            if task_text.strip():  # Ensure task is not empty
                ListItem.objects.create(name=task_text, anchorcheckpoint_id=id)
            return redirect("timeline:list_task")
    else:
        context = {'anchor_obj':anchor_obj}
    return render(request,"timeline/addtask.html", context)

def create_parent(request):
    if request.method == "POST":
        form = CreateDailyForm(request.POST)
        if form.is_valid():
            instance = form.save()
            anchor = AnchorCheckPoint.objects.create(dailyparent_id=instance.id)
            print(f"Anchor ID: {anchor.id}")
            anchro_id = anchor.id
            url = reverse("timeline:task_add", kwargs={'id':anchor.id})
            return redirect(url)
         
    else:
        form = CreateDailyForm()
    return render(request, 'timeline/parent.html', {'form': form})


def parent_list(request):
    objs =  DailyParent.objects.all()
    context = {'objs':objs}
    return render(request,'timeline/list.html', context)



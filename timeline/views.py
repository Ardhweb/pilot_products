from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from .models import ParentTask, ListItem
from .forms import CreateDailyForm
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def anchorpoint(request, id):
    try:
        anchor_obj = ParentTask.objects.get(pk=id)
    except ParentTask.DoesNotExist:
        return render(request, "timeline/error.html", {"message": "parent_task not found."})
    list_items = ListItem.objects.filter(parent_task_id=id)
    if request.method == "POST":
        tasks = request.POST.getlist("task[]")  # Get all task inputs with the same name
        print(tasks)
        if tasks:
            # Create a list of ListItem instances using the tasks data
            list_items = [ListItem(name=task, parent_task_id=id) for task in tasks]
            # Bulk create the ListItem objects
            ListItem.objects.bulk_create(list_items)
            return redirect("timeline:list_task")
    else:
        context = {'anchor_obj': anchor_obj,'list_items':list_items}
    return render(request, "timeline/addtask.html", context)

@login_required
def create_parent(request):
    if request.method == "POST":
        form = CreateDailyForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            url = reverse("timeline:task_add", kwargs={'id':instance.id})
            return redirect(url)
    else:
        form = CreateDailyForm()
    return render(request, 'timeline/parent.html', {'form': form})

@login_required
def parent_list(request):
    anchor = ParentTask.objects.filter(user_id=request.user.id).prefetch_related('listitem_set')
    context = {"anchor":anchor}
    return render(request,'timeline/list.html', context)



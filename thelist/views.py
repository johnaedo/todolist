from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from thelist.models import Tasks
from thelist.forms import TaskForm
from datetime import date
import re

def index(request):
    tasks = Tasks.objects.all()
    return render(request, "index.html", {"tasks" : tasks})

def addTask(request):
    # newTask = Tasks(descr=request.POST['task'],
    #                completed=False)
    # newTask.save()
    # return render(request, "index.html")
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the task to the database
            return redirect('/')  # You can replace 'task_list' with the URL name of your task list view
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})



def updateList(request):
    updatedTasks = {}
    for key, value in request.POST.items():
        res = re.search(r"(\d+)-completed", key)
        if (res):
            updatedTasks[res.group(1)] = value

    for key in updatedTasks:
        updatedTask = Tasks.objects.get(id=key)
        updatedTask.completed = True
        updatedTask.dateCompleted = date.today()
        updatedTask.save()


    return render(request, "updateDump.html", {"formInput": request.POST})

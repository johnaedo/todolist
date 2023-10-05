from django.shortcuts import HttpResponse
from django.shortcuts import render
from thelist.models import Tasks
from datetime import date

def index(request):
    tasks = Tasks.objects.all()
    return render(request, "index.html", {"tasks" : tasks})

def addTask(request):
    newTask = Tasks(descr=request.POST['task'],
                    completed=False)
    newTask.save()
    return render(request, "index.html")

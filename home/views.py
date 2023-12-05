# views.py
from django.shortcuts import render
from .models import Task

def home(request):
    context = {'success': False}

    if request.method == "POST":
        # Handle the form
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        print(title, desc)

        # Try to create a Task instance and save it to the database
        try:
            ins = Task(taskTitle=title, taskDesc=desc)
            ins.save()
            context = {'success': True}
        except Exception as e:
            print(f"Error saving Task instance: {e}")

    return render(request, 'index.html', context)


def task(request):
    allTasks = Task.objects.all()
    print(allTasks)
    context = {'task': allTasks}

    # for item in allTasks:
    #     print(item.taskTitle)

    return render(request, 'task.html', context)
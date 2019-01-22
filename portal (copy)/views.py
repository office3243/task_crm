from django.shortcuts import render
from .models import Task
from django.shortcuts import get_object_or_404, get_list_or_404
from datetime import date
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        try:
            return render(request, 'portal/home.html', {'employee': request.user.employee})
        except:
            return render(request, 'portal/home.html', {'employee': None})
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
def my_tasks(request):
    try:
        completed_tasks = get_list_or_404(Task, employee=request.user.employee, submitted=True)
        pending_tasks = get_list_or_404(Task, employee=request.user.employee, submitted=False)
        return render(request, 'portal/my_tasks.html', {'completed_tasks': completed_tasks, 'pending_tasks': pending_tasks, 'employee': request.user.employee})
    except :
        return HttpResponse("User has no employee")



@login_required
def task_details(request, task_id):
    return render(request, 'portal/task_details.html', {'task': get_object_or_404(Task, id=task_id)})

@login_required
def submit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.submitted = True
    task.submitted_on = date.today()
    task.save()
    return HttpResponseRedirect('/my_tasks/')

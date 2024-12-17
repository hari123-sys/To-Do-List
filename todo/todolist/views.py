from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .models import ToDo
from django.utils import timezone


def index(request,*args):

    context = {
          'title':"To Do Lists",
        }  

    if request.method == "POST":
        search = request.POST.get('search')
        details = ToDo.objects.filter(title__icontains = search).order_by('-time')

    elif args:
        details = ToDo.objects.all().filter(status = args[0]).order_by("-time")
        context['title'] = 'Completed ' + context['title']
    else:
         details = ToDo.objects.all().filter(status = 'Not Completed').order_by("-time")

    def concat(todo):
        return '-'.join(todo.title.split())
    
    context['todo_lists'] = zip(map(concat,details),details)

    return render(request,'index.html',context) 


def todo_form(request,**args):

    context = {
        'title':'create an activity', 
        'todotitle':'',
        'desc':''
    }

    if args:
        details = ToDo.objects.get(id = args['id'])
        context['todotitle'] = details.title
        context['desc'] = details.desc

    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')

        if args:
            details.title = title
            details.desc = desc
            details.time = timezone.now()
            details.status = 'Not Completed'
        else:
            details = ToDo(title = title,desc = desc)
        
        details.save()
        
        return redirect('home')
    else:
        return render(request,'TodoForm.html',context)
    

def viewData(request,title):
    details = ToDo.objects.all().order_by("-time")
    title = separate(title)
    desc = ''
    time = ''
    id = 0
    for todo in details:
        if todo.title == title:
            desc = todo.desc
            time = todo.time
            id = todo.id
            break
    
    return render(request,'viewData.html',{'id':id, "title":title, 'desc':desc, 'time':time})


def separate(todo_title):
    return ' '.join(todo_title.split('-'))


def delete_todo(request,id):
    record = ToDo.objects.get(id = id)
    record.delete()
    home_url = reverse('home')
    return index(request,'Completed') 
 

def editTodo(request,id):
    return todo_form(request,id = id)


def done(requests,id):
    record = ToDo.objects.get(id = id)
    record.status = 'Completed'
    record.time = timezone.now()
    record.save()
    home_url = reverse('home')
    return redirect(home_url) 


def completedTasks(request):
    return index(request,'Completed')







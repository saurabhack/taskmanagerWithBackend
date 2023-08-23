from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import todo,hist
from django.contrib import messages
from .forms import TodoForm
# Create your views here.
def show(request):
    
    if request.method=='POST':
        query=request.POST['search']
        if query:
            results=todo.objects.filter(title__contains=query)
            return render(request,'show.html',{'results':results})
        else:
            messages.info(request,'information is not available')
            return render(request,'show.html',{})
    return render(request,'show.html')
def index(request):
    item_list = todo.objects.order_by("-date")
    if request.method == "POST":
        form =TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = TodoForm()
 
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'index.html', page)
 
def remove(request,item_id):
    item=todo.objects.get(id=item_id)
    item.delete()
    hist.objects.create(name=item.title,action="uncompleted")
    messages.info(request,'task is removed !!!')
    return redirect('/')

def complete(request, item_id):
    item = todo.objects.get(id=item_id)
    
    if item:
        
        hist.objects.create(name=item.title,action="completed")
        item.delete()
        messages.success(request, "Task marked as completed")
    else:
        messages.warning(request, "Task is already completed")
        
    
    return redirect('/')
def form(request):
    if request.method=='POST':
        forms=TodoForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    else:
        forms= TodoForm()
        return render(request,'form.html',{'forms':forms})
def history(request):
    history_list = hist.objects.all().order_by('id')
    return render(request, 'history.html', {'history_list': history_list})


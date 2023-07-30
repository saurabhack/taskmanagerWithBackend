from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todo
from django.contrib import messages
from .forms import TodoForm
# Create your views here.
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
    messages.info(request,'item removed !!!')
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
def complete(request):
    '''
    item=todo.objects.get(id=item_id)
    if item:
        temp='this task is completed'
        return render(request,'index.html',{'temp':temp})
    else:
        return redirect('/')'''
    temp= HttpResponse('this task is completed')
    return render(request,'index.html',{'temp':temp})
    
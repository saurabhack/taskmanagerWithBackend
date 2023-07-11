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

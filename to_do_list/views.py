from django.http import response
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import ToDoItem
from .forms import ToDoForm

# Create your views here.

def item_list(request):
    items = ToDoItem.objects.all()
    form = ToDoForm()

    if request.method == 'POST':
        print("masuk 1")
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            print("masuk 2")
        return redirect('/') # redirect ke halaman ini lagi. tapi kok ga bisa ya?

    context = {'items':items, 'form':form}
    return render(request, 'item_list.html', context)

def item_detail(request, pk): #primary key
    item = ToDoItem.objects.get(id=pk)
    form = ToDoForm(instance=item)

    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'item_detail.html', context)
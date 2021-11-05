from django.http import response
from django.shortcuts import get_object_or_404, render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import ToDoItem
from .forms import ToDoForm

def todo_index(request):
    todos = ToDoItem.objects.all()
    form = ToDoForm()

    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
        return redirect('/to-do-list/')
        
    context = {'todos':todos, 'form':form}
    return render(request, 'todo_index.html', context)

def todo_detail(request, id):
    context = {}
    todo = get_object_or_404(ToDoItem, id=id)
    form = ToDoForm(request.POST or None, instance=todo)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/to-do-list/')
        
    context['form'] = form
    return render(request, 'todo_detail.html', context)

def todo_delete(request):
    if request.method == 'POST':
        todo_name = request.POST.get('todo_name')
        ToDoItem.objects.filter(title=todo_name).delete()
        return JsonResponse({'status':'deleted'})
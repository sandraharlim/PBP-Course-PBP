from django.http import response
from django.core import serializers
from django.shortcuts import get_object_or_404, render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import ToDoItem
from .forms import ToDoForm
from .serializers import ToDoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

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

def json(request):
    data = serializers.serialize('json', ToDoItem.objects.all())
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
@api_view(['POST'])
def from_dart(request):
    serializer = ToDoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
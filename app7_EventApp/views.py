from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Event
from .forms import EventForm
import operator
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.http import JsonResponse


# Create your views here.
@login_required(login_url='/login')
def index (request):
    dateOrder = Event.objects.order_by('Time')
    ordered = sorted(dateOrder, key=operator.attrgetter('Time'))
    response = {'event':ordered}
    return render(request, "index.html", response)

@login_required(login_url='/login')
def add_event (request):
    context = {}
    form = EventForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # save the form data to model
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        form = EventForm()
        return HttpResponseRedirect("/EventApp")
    
    context['form']= form
    return render(request, "addEvent.html", context)


@login_required(login_url='/login')
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Event, id = id)
 
    # pass the object as instance in form
    form = EventForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/EventApp")
 
    # add form dictionary to context
    context["form"] = form
    context["object"] = obj
 
    return render(request, "update_view.html", context)


class DeleteCrudUser(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Event.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
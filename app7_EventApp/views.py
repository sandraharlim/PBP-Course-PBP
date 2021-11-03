from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Event
from .forms import EventForm
import operator


# Create your views here.
def index (request):
    dateOrder = Event.objects.order_by('Time')
    ordered = sorted(dateOrder, key=operator.attrgetter('Time'))
    response = {'event':ordered}
    return render(request, "index.html", response)

def add_event (request):
    context = {}

    form = EventForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        # save the form data to model
        form.save()
        form = EventForm()
        return HttpResponseRedirect("/EventApp")

    context['form']= form
    return render(request, "addEvent.html", context)
def manage_view (request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    dateOrder = Event.objects.order_by('Time')
    ordered = sorted(dateOrder, key=operator.attrgetter('Time'))
 
    # add the dictionary during initialization
    context["dataset"] = ordered
         
    return render(request, "manage_view.html", context)

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
        return HttpResponseRedirect("/EventApp/ManageEvent")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)

def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Event, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/EventApp/ManageEvent")
 
    return render(request, "delete_view.html", context)

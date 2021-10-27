from django.shortcuts import render
from .models import Event
from .forms import EventForm

# Create your views here.
def index (request):
    event = Event.objects.all().values()
    response = {'event':event}
    return render(request, "index.html", response)

def add_event (request):
    context = {}

    form = EventForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        # save the form data to model
        form.save()
        form = EventForm()

    context['form']= form
    return render(request, "addEvent.html", context)



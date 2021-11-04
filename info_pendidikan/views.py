from django.http import response
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import InfoPendidikan
from .forms import infoForm

# Create your views here.

def info_pendidikan(request):
    items = InfoPendidikan.objects.all()
    form = infoForm()

    if request.method == 'POST':
        form = infoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/info-pendidikan')

    context = {
        'form':form,
        'items':items,
        }
    return render(request, 'index.html', context)
from django.http import response
from django.shortcuts import redirect, render
from .models import Matkul
from .forms import MatkulForm
import operator
from django.core import serializers
from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/admin/login/')
# def index(request):
#     matkul_list = Matkul.objects.all()
#     matkul_list_ordered = sorted(matkul_list, key=operator.attrgetter("day", "start_time", "name"))
#     response = {'matkuls' : matkul_list,
#                 'matkuls_ordered' : matkul_list_ordered}
#     return render(request, 'app1_index.html', response)

@login_required(login_url='/admin/login/')
def matkul_list(request):
    matkuls = Matkul.objects.all()  
    matkuls_ordered = sorted(matkuls, key=operator.attrgetter("day","start_time", "name"))
    response = {'matkuls': matkuls,
                'matkuls_ordered' : matkuls_ordered,}
    return render(request, 'app1_matkul_list.html', response)

@login_required(login_url='/admin/login/')
def json(request):
    matkuls = Matkul.objects.all()  
    matkuls_ordered = sorted(matkuls, key=operator.attrgetter("day","start_time", "name"))
    data = serializers.serialize('json', matkuls_ordered)
    return HttpResponse(data, content_type="application/json")

@login_required(login_url='/admin/login/')
def add_matkul(request):
    response = {}
    form = MatkulForm(request.POST or None)
    if (request.method == 'POST' and form.is_valid):
        form.save()
        return HttpResponseRedirect('/app-1/')
    response['form'] = form
    matkul_list = Matkul.objects.all()
    matkul_list_ordered = sorted(matkul_list, key=operator.attrgetter("day", "start_time", "name"))
    response['matkuls_ordered'] = matkul_list_ordered
    return render(request, "app1_index.html", response)

@login_required(login_url='/admin/login/')
def edit_matkul(request):
    # response = {}
    # matkul = Matkul.objects.get(id=name)
    # form = MatkulForm(request.POST or none)
    # if (request.method == 'POST' and form.is_valid):
    #     form.save()
    #     return HttpResponseRedirect('/app-1/matkul_list/')
    # response['form'] = form
    # response['matkul'] = matkul
    # return render(request, "app1_edit.html", response)

    if (request.method == 'POST'):
        matkul_name = request.POST.get("name")
        matkul_day = request.POST.get("day")
        matkul_start_time = request.POST.get("start_time")
        matkul_end_time = request.POST.get("end_time")

        matkul = Matkul.objects.get(id=matkul_name)
        matkul.name = matkul_name
        matkul.day = matkul_day
        matkul.start_time = matkul_start_time
        matkul.end_time = matkul_end_time
        return HttpResponseRedirect('/app-1/matkul_list/')

@login_required(login_url='/admin/login/')
def delete_matkul(request):
    if (request.method == "POST"):
        matkul_name = request.POST.get("name")
        matkul = Matkul.objects.get(id=matkul_name)
        matkul.delete()
        return HttpResponseRedirect('/app-1/matkul-list/')

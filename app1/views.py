from django.shortcuts import render
from .models import Matkul
import operator
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def matkul_list(request):
    matkuls = Matkul.objects.all()  
    # matkuls_ordered = sorted(matkuls, key=operator.attrgetter("day","start_time", "name"))
    return JsonResponse({'matkul' : list(matkuls.values())})

@login_required(login_url='/login')
def home(request):
    return render(request, 'app1_home.html')

# Referensi : https://dontrepeatyourself.org/post/django-todo-app-with-ajax-and-jquery/
def matkul_create(request):
    if request.method == 'POST':
        matkul_name = request.POST.get('matkul_name')
        matkul_day = request.POST.get('matkul_day')
        matkul_start_time = request.POST.get('matkul_start_time')
        matkul_end_time = request.POST.get('matkul_end_time')

        matkul = Matkul.objects.filter(author=request.user, name=matkul_name)
        # we need to make sure that this matkul does not exist in the database
        if matkul.exists():
            return JsonResponse({'status': 'error'})

        matkul = Matkul.objects.create(author=request.user, name=matkul_name, day=matkul_day, 
                start_time=matkul_start_time, end_time=matkul_end_time) 
        return JsonResponse({'matkul_name': matkul.name, 'matkul_day' : matkul.day,
                'matkul_start_time': matkul.start_time, 'matkul_end_time': matkul.end_time,
                'status' : 'created'})  

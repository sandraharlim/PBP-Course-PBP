from django.http import JsonResponse
from django.shortcuts import render
from .forms import AddInfoPandemi, AddTipsKesehatan, AddCurahanHati
from .models import InfoPandemi, TipsKesehatan, CurahanHati

# Create your views here.
def add_info_pandemi(request):
    form = AddInfoPandemi()
    forum = InfoPandemi.objects.all().order_by('-id').distinct()
    if request.is_ajax():
        form = AddInfoPandemi(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    listNama = InfoPandemi.objects.all()
    return render(request, 'add_infopandemi.html', {'form': form, 'forum': forum, 'listNama': listNama})

def add_tips_kesehatan(request):
    form = AddTipsKesehatan()
    forum = TipsKesehatan.objects.all().order_by('-id').distinct()
    if request.is_ajax():
        form = AddTipsKesehatan(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    listNama = TipsKesehatan.objects.all()
    return render(request, 'add_tipskesehatan.html', {'form': form, 'forum': forum, 'listNama': listNama})

def add_curahan_hati(request):
    form = AddCurahanHati()
    forum = CurahanHati.objects.all().order_by('-id').distinct()
    if request.is_ajax():
        form = AddCurahanHati(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    listNama = CurahanHati.objects.all()
    return render(request, 'add_curahanhati.html', {'form': form, 'forum': forum, 'listNama': listNama})

def button(request):
    return render(request, 'buttons.html', {})

def search_info_pandemi(request):
    form = AddInfoPandemi()
    # forum = ForumPertanyaan.objects.all().order_by('-id').distinct()
    yang_ingin_dicari = request.GET.get('kotak_cari')
    forum_filter = InfoPandemi.objects.filter(nama__icontains = yang_ingin_dicari).order_by('-id')
    if request.is_ajax():
        form = AddInfoPandemi(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'add_infopandemi.html', {'form': form, 'forum': forum_filter})

def search_tips_kesehatan(request):
    form = AddTipsKesehatan()
    # forum = ForumPertanyaan.objects.all().order_by('-id').distinct()
    yang_ingin_dicari = request.GET.get('kotak_cari')
    forum_filter = TipsKesehatan.objects.filter(nama__icontains = yang_ingin_dicari).order_by('-id')
    if request.is_ajax():
        form = AddTipsKesehatan(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'add_tipskesehatan.html', {'form': form, 'forum': forum_filter})

def search_curahan_hati(request):
    form = AddCurahanHati()
    # forum = ForumPertanyaan.objects.all().order_by('-id').distinct()
    yang_ingin_dicari = request.GET.get('kotak_cari')
    forum_filter = CurahanHati.objects.filter(nama__icontains = yang_ingin_dicari).order_by('-id')
    if request.is_ajax():
        form = AddCurahanHati(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'add_curahanhati.html', {'form': form, 'forum': forum_filter})

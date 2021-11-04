from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.template import loader
from .forms import SearchForm
import requests
from .models import SearchedCovidData


def covid_data(request):
    searched_data = SearchedCovidData.objects.all().values()
    form = SearchForm(request.POST or None)
    response = requests.get('https://data.covid19.go.id/public/api/prov_list.json')
    try:
        data = response.json()
    except:
        data = None
    kasus = []
    error = None
    searched_provinsi = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                searched_provinsi = form.cleaned_data['provinsi']
    if data is not None:
        for o in data['list_data']:
            datanya = {}
            datanya['provinsi'] = o['key']
            datanya['kasus_positif'] = o['status']['buckets'][2]['doc_count']
            datanya['kasus_sembuh'] = o['status']['buckets'][0]['doc_count']
            datanya['kasus_meninggal'] = o['status']['buckets'][1]['doc_count']
            if searched_provinsi != None:
                if datanya['provinsi'] in searched_provinsi:
                    new = SearchedCovidData(user = request.user,provinsi=datanya['provinsi'], kasus_positif=datanya['kasus_positif'],kasus_sembuh=datanya['kasus_sembuh'],kasus_meninggal=datanya['kasus_meninggal'])
                    new.save()
            kasus.append(datanya)
    else:
        error = "Maaf sumber data yang kami pakai sedang bermasalah"
    return render(request, 'covid_data.html', {
        'searched_data': searched_data,
        'form': form,
        'error': error,
        'date':data['last_date'],
        })

def search(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        search_key = request.GET.get('search')
        response = requests.get('https://data.covid19.go.id/public/api/prov_list.json')
        data = response.json()
        kasus = []
        for o in data['list_data']:
            datanya = {}
            datanya['provinsi'] = o['key']
            datanya['kasus_positif'] = o['status']['buckets'][2]['doc_count']
            datanya['kasus_sembuh'] = o['status']['buckets'][0]['doc_count']
            datanya['kasus_meninggal'] = o['status']['buckets'][1]['doc_count']
            if request.user.is_authenticated:
                if datanya['provinsi'] in search_key:
                    new = SearchedCovidData(author = request.user,provinsi=datanya['provinsi'], kasus_positif=datanya['kasus_positif'],kasus_sembuh=datanya['kasus_sembuh'],kasus_meninggal=datanya['kasus_meninggal'])
                    new.save()
            kasus.append(datanya)
        
        data_html = loader.render_to_string(
            'data.html',
            {'data': kasus, 'search_key': search_key}
        )
        output_data = {
            'data_html': data_html,
        }
        return JsonResponse(output_data, status=200)
    # some error occured
    return JsonResponse({"error": ""}, status=400)
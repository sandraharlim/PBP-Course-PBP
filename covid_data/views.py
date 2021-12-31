from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.template import loader
from .forms import SearchForm
import requests
from .models import SearchedCovidData
from django.views.decorators.csrf import csrf_exempt
from django.forms import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
from django.core import serializers
import json
class ExtendedEncoder(DjangoJSONEncoder):

    def default(self, o):

        if isinstance(o, Model):
            return model_to_dict(o)

        return super().default(o)

def covid_data(request):
    searched_data = SearchedCovidData.objects.all().order_by('-id')
    form = SearchForm(request.POST or None)
    response = requests.get('https://data.covid19.go.id/public/api/prov_list.json')
    try:
        data = response.json()
    except:
        data = None
    kasus = []
    error = None
    if data is not None:
        for o in data['list_data']:
            datanya = {}
            datanya['provinsi'] = o['key']
            datanya['kasus_positif'] = o['status']['buckets'][2]['doc_count']
            datanya['kasus_sembuh'] = o['status']['buckets'][0]['doc_count']
            datanya['kasus_meninggal'] = o['status']['buckets'][1]['doc_count']
            kasus.append(datanya)
    else:
        error = "Maaf sumber data yang kami pakai sedang bermasalah"
    return render(request, 'covid_data.html', {
        'searched_data': searched_data,
        'form': form,
        'error': error,
        'date':data['last_date'],
        })

@csrf_exempt
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
            {'data': kasus, 'search_key': search_key, 'date':data['last_date'],}
        )
        output_data = {
            'data_html': data_html,
        }
        return JsonResponse(output_data, status=200)
    # some error occured
    return JsonResponse({"error": ""}, status=400)

def searchF(request):
    # request should be ajax and method should be GET.
    if request.method == "GET":
        search_key = request.GET.get('search')
        curr_user_id = request.GET.get('user_id')
        response = requests.get('https://data.covid19.go.id/public/api/prov_list.json')
        data = response.json()
        searchedData = {}
        for o in data['list_data']:
            if o['key'] in search_key:
                searchedData['provinsi'] = o['key']
                searchedData['kasus_positif'] = o['status']['buckets'][2]['doc_count']
                searchedData['kasus_sembuh'] = o['status']['buckets'][0]['doc_count']
                searchedData['kasus_meninggal'] = o['status']['buckets'][1]['doc_count']
                if curr_user_id != "":
                    new = SearchedCovidData(author = User.objects.get(pk = curr_user_id),provinsi=searchedData['provinsi'], kasus_positif=searchedData['kasus_positif'],kasus_sembuh=searchedData['kasus_sembuh'],kasus_meninggal=searchedData['kasus_meninggal'])
                    new.save()
                return JsonResponse({'searchedData':searchedData}, status=200)
    # some error occured
    return JsonResponse({"error": ""}, status=400)

def getModelsF(request):
    if request.method == "GET":
        curr_user_id = int(request.GET.get('user_id'))
        searchedData = SearchedCovidData.objects.filter(author = User.objects.get(pk = curr_user_id)).order_by('-id')
        tmpJson = serializers.serialize("json",searchedData)
        tmpObj = json.loads(tmpJson)
        return JsonResponse({"searchedData": tmpObj},encoder=ExtendedEncoder, status=200)
    # some error occured
    return JsonResponse({"error": ""}, status=400)
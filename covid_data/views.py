from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.template import loader
from .forms import SearchForm
from .models import SearchedCovidData
import requests

def covid_data(request):
    #searched_data = SearchedCovidData.objects.all()
    form = SearchForm(request.POST)
    response = requests.get('https://api.kawalcorona.com/indonesia/provinsi')
    data = response.json()
    kasus = []
    searched_provinsi = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                searched_provinsi = form.cleaned_data['provinsi']
    for o in data:
        datanya = {}
        datanya['provinsi'] = o['attributes']['Provinsi']
        datanya['kasus_positif'] = o['attributes']['Kasus_Posi']
        datanya['kasus_sembuh'] = o['attributes']['Kasus_Semb']
        datanya['kasus_meninggal'] = o['attributes']['Kasus_Meni']
        #if searched_provinsi != None:
            #if datanya['provinsi'] == searched_provinsi:
                #SearchedCovidData.objects.create(
                   #provinsi=datanya['provinsi'], kasus_positif=datanya['kasus_positif'],kasus_sembuh=datanya['kasus_sembuh'],kasus_meninggal=datanya['kasus_meninggal']
                   # )
        kasus.append(datanya)

    return render(request, 'covid_data.html', {
        'data': kasus,
        'searched_data': searched_data,
        'form': form
        })

#def process_covid_data(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = FriendForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)

def search(request):
    response = requests.get('https://api.kawalcorona.com/indonesia/provinsi')
    data = response.json()
    kasus = []
    for o in data:
        datanya = {}
        datanya['provinsi'] = o['attributes']['Provinsi']
        datanya['kasus_positif'] = o['attributes']['Kasus_Posi']
        datanya['kasus_sembuh'] = o['attributes']['Kasus_Semb']
        datanya['kasus_meninggal'] = o['attributes']['Kasus_Meni']
        kasus.append(datanya)
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        search_key = request.GET.get('search')
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
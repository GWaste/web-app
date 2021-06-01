from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from pathlib import Path
from io import BytesIO
from base64 import b64decode
import json
import requests

CONFIG_DIR = Path(__file__).parent.parent.joinpath('config')
UKM, PRODUCTS, CATEGORIES = {}, {}, {}
with open(CONFIG_DIR.as_posix() + '/ukm.json', 'r') as f:
    for ukm in json.load(f)['ukm']:
        UKM[ukm['id']] = ukm
with open(CONFIG_DIR.as_posix() + '/product.json', 'r') as f:
    for product in json.load(f)['products']:
        PRODUCTS[product['id']] = product
with open(CONFIG_DIR.as_posix() + '/category.json', 'r') as f:
    for category in json.load(f)['category']:
        CATEGORIES[category['id']] = category
        CATEGORIES[category['name'].lower()] = category

def home(request):
    return render(request, 'home.html')

def camera(request):
    return render(request, 'camera.html')

def predict(request):
    requestJson = json.loads(request.body)
    imgBase64 = requestJson['imgBase64'].split("base64,")[1]

    # untuk coba coba, mungkin ini dibikin False aja biar gak panggil API terus
    if True:
        response = requests.post('https://us-central1-cosmic-quarter-312712.cloudfunctions.net/waste-classifier', json={
            "image": imgBase64
        })
        predictions = sorted(response.json(), key=lambda x: x['confident'], reverse=True)
    else:
        predictions = [{'name': 'cardboard', 'confident': 0.9330371618270874}, {'name': 'paper', 'confident': 0.06237144023180008}, {'name': 'plastic', 'confident': 0.0027473338413983583}, {'name': 'glass', 'confident': 0.0011992143699899316}, {'name': 'metal', 'confident': 0.0006447614287026227}]

    return JsonResponse(predictions[0:2], safe=False)

def favorites(request):
    return HttpResponse('')

def category(request, category_name=''):
    return HttpResponse('')
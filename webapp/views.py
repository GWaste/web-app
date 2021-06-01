from django.shortcuts import render
from django.http.response import Http404, HttpResponse, JsonResponse
from pathlib import Path
from io import BytesIO
from base64 import b64decode
import json
import requests

CONFIG_DIR = Path(__file__).parent.parent.joinpath('config')
UKM, PRODUCTS, CATEGORIES = {}, {}, {}
with open(CONFIG_DIR.as_posix() + '/category.json', 'r') as f:
    for category in json.load(f)['category']:
        category['products'] = []
        CATEGORIES[category['id']] = category
        CATEGORIES[category['name'].lower()] = category
with open(CONFIG_DIR.as_posix() + '/product.json', 'r') as f:
    for product in json.load(f)['products']:
        product['ukm'] = []
        PRODUCTS[product['id']] = product
        CATEGORIES[product['category_id']]['products'].append(product)
with open(CONFIG_DIR.as_posix() + '/ukm.json', 'r') as f:
    for ukm in json.load(f)['ukm']:
        if ukm['contact']['instagram'] != None:
            ukm['contact']['instagram'] = ukm['contact']['instagram'][1:]
        ukm['products'] = []
        for product_id in ukm['product_id']:
            product = PRODUCTS[product_id]
            product['ukm'].append(ukm)
            ukm['products'].append(product)
        UKM[ukm['id']] = ukm

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
    return HttpResponse('not implemented yet')

def category(request, category_name=''):
    category_name = category_name.lower()
    if category_name not in CATEGORIES:
        raise Http404("Category does not exist")
    return render(request, 'category.html', {
        "category_name": category_name.capitalize(),
        "products": CATEGORIES[category_name]['products']
    })

def product(request, product_id):
    if product_id not in PRODUCTS:
        raise Http404("Product does not exist")
    product = PRODUCTS[product_id]
    product['embed_yt'] = "https://youtube.com/embed/" + product['link_yt'].split("?v=")[1]
    return render(request, 'product.html', {
        "product": PRODUCTS[product_id]
    })
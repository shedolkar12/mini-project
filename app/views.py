from django.shortcuts import render, HttpResponse, render_to_response 
#from django.http import JsonResponse
from app.models import *
from django.core import serializers
import json

START_DATE = "1800-01-01"
END_DATE = "2030-01-01"

def dashboard(request):
    p = Soldiers.objects.all()
    data = serializers.serialize('json', p)
    p = []
    data = json.loads(data)
    for d in data:
        p.append(d['fields'])       
    return render_to_response('index.html', {"data": p })

def index(request):
    start_date = START_DATE
    end_date = END_DATE
    data = {}
    for i in  ['option', 'start_date', 'end_date']:
        if i not in request.GET:
            if i=='option':
                data[i] = '0'
            elif i=='start_get':
                data[i] = START_DATE
            else:
                data[i] = END_DATE
        else:
            data[i] = request.GET[i]
    # In Case if date field is epmty using                                   
    if data['start_date']:
        start_date = data['start_date']
    if data['end_date']:     
        end_date = data['end_date']
     
    if data['option'] == '0':
        data = Soldiers.objects.all()
        result = []
        for d in data:
            if start_date <= d.join_date and d.join_date <= end_date:
                result.append(d)
    elif data['option'] == '1':
        result = []
        data = Weapons.objects.all()
        for d in data:
            if start_date <= d.available and d.available <= end_date:
                result.append(d)        
    else:
        data = Food.objects.all()
        result = []
        for d in data:
            if start_date <= d.expire and d.expire <= end_date:
                result.append(d)
  
    data = serializers.serialize('json', result)
    json_data = []
    data = json.loads(data)
    for d in data:
        json_data.append(d['fields'])
    return HttpResponse(json.dumps(json_data), content_type='application/json')
# Create your views here.

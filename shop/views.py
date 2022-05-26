from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.core import serializers
from . models import Shop
"""
requests.method => GET,POST,UPDATE if 
get => requsts.GET 
post => requersts.POST

"""
pair = ['name','category','subcategory','amount']
def keys(value:dict):
  keylist= list(value.keys())
  if len(keylist) != len(pair):
    return False
  return sorted(keylist) == sorted(pair)



def getreq(data:dict):
  if not bool(data):
    wholedata= Shop.objects.all()
    serilize = serializers.serialize('json', wholedata)
    return JsonResponse(serilize,safe=False)
  else:
    key=str(list(data.keys())[0])
    if key == "name":
      return JsonResponse(serializers.serialize('python',Shop.objects.filter(name=str(data[key][0]))),safe=False)
    elif key == "category":
      return JsonResponse(serializers.serialize('python',Shop.objects.filter(category=str(data[key][0]))),safe=False)
    elif key == "subcategory":
      return JsonResponse(serializers.serialize('python',Shop.objects.filter(subcategory=str(data[key][0]))),safe=False)
    elif key == "amount":
      return JsonResponse(serializers.serialize('python',Shop.objects.filter(amount=str(data[key][0]))),safe=False)
    else:
      return JsonResponse({"Error":"400"},safe=False,status=400)
      

def postreq(data:dict):
  if keys(data):
    database = Shop.objects.create(
      name=str(data['name'][0]),
      category=str(data['category'][0]),
      subcategory=str(data['subcategory'][0]),
      amount=int(data['amount'][0])
    )
    return JsonResponse({'Success':'200'},status=200,safe=False)
  return JsonResponse({"Error":"400"},safe=False,status=400)


def putreq(data:dict):
  if keys(data):
    if Shop.objects.filter(name=str(data['name'][0])).exists():
       s = Shop.objects.get(name=str(data['name'][0]))
       s.category = str(data['category'][0])
       s.subcategory = str(data['subcategory'][0])
       s.amount = int(data['amount'][0])
       s.save()
    else:
      database = Shop.objects.create(
      name=str(data['name'][0]),
      category=str(data['category'][0]),
      subcategory=str(data['subcategory'][0]),
      amount=int(data['amount'][0])
    )
    return JsonResponse({'Success':'200'},status=200,safe=False)
  return JsonResponse({"Error":"400"},safe=False,status=400)

@csrf_exempt
def shop(requests):
  if requests.method=="GET":
    return getreq(dict(requests.GET))
  elif requests.method=="POST":
    return postreq(dict(requests.GET))
  elif requests.method == "PUT":
    return putreq(dict(requests.GET))
      
  return JsonResponse({}, safe= False)
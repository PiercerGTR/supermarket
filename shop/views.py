from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core import serializers
from . models import Shop
"""
requests.method => GET,POST,UPDATE if 
get => requsts.GET 
post => requersts.POST

"""
def index(request):
  allitems = Shop.objects.all().values()
  output = ""
  for x in allitems:
    output += x["name"]
  return HttpResponse(output)

def shop(requests):
      wholedata= Shop.objects.all()
      serilize = serializers.serialize('json', wholedata)
      return JsonResponse(serilize, safe= False)
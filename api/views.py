from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
import json

from resto.models import Rest
from resto.models import Items

# Create your views here.
def index(request):
        rest_list = Rest.objects.all()
    #    context = {'rest_list': rest_list}
        dict={}
        lst=[]
        for r in rest_list:
            dict={
            "name":r.name_text,
            "address":r.address_text
            }
            lst.append(dict)
        return HttpResponse(json.dumps(lst))
       # return render(request, 'api/index.html', context)
       # return HttpResponse("Hello")

def details(request,rest_id):
    rest1 = Rest.objects.filter(pk=rest_id).first()
    items = Items.objects.filter(rest=rest1)
    if not rest1:
        raise Http404("Restaurent does not exist")
    else:
    #    context = {'rest1' : rest1,'items':items}
    #    return render(request,'resto/details.html',context)
        itms=[]
        dict={}

        for i in items:
            dict={
            "dish name":i.dish_text,
            "price":str(i.price)
            }
            itms.append(dict)
        i={
        'name':rest1.name_text,
        'address':rest1.address_text,
        'items':itms
        }

        return HttpResponse(json.dumps(i))

@csrf_exempt
def createnew(request):
    if request.method == 'POST':
        r = Rest(name_text=request.POST.get("name"), 
        address_text=request.POST.get("add"))
        r.save()
        return HttpResponse("Added succussfully")
    elif request.method == 'GET':
        return HttpResponse("Unauthorised access to database")

@csrf_exempt
def createnewitems(request,rest_id): 
    if request.method == 'POST':
        rest1 = Rest.objects.filter(pk=rest_id).first()
        i = Items(dish_text=request.POST.get("name1"), 
        price=request.POST.get("price"),rest=rest1)
        i.save()
        return HttpResponse("Added succussfully")
    elif request.method == 'GET':
        return HttpResponse("Unauthorised access to database")

@csrf_exempt
def countR(request):
    
    return HttpResponse(Rest.objects.all().count())
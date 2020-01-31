from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.parse
from django.contrib.sessions.models import Session
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from resto.models import Rest
from resto.models import Items
from resto.models import Order
from resto.models import OrderItems




# Create your views here.
@login_required
def index(request):
    id=request.user
    print(id)
    rest_list = Rest.objects.all()
    #    context = {'rest_list': rest_list}
    paginator = Paginator(rest_list,12)
    num=paginator.num_pages
    
    page = request.GET.get('page')
    lis=[]
    lis = paginator.get_page(page)
    #print(page)
   # print(num)
  #  print (type(page), type(num))

    if str(num)==page:
        dict={}
        lst=[]
        for r in lis:
            dict={
            "id":r.id,
            "name":r.name_text,
            "address":r.address_text,
            "nextpage":0,
            }
            lst.append(dict)
    elif str(num)!=page:
        dict={}
        lst=[]
        for r in lis:
            dict={
            "id":r.id,
            "name":r.name_text,
            "address":r.address_text,
            "nextpage":1,
            }
            lst.append(dict)
    return HttpResponse(json.dumps(lst))
       # return render(request, 'api/index.html', context)
       # return HttpResponse("Hello")



@login_required
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
            "id":i.id,
            "dish_name":i.dish_text,
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
@login_required
def createnew(request):
    print(request)
    if request.method == 'POST':
        json_data=json.loads(request.body)
        print(type(json_data))
        r = Rest(name_text=json_data.get("name"), 
        address_text=json_data.get('address'))                      #json_data['name']
        r.save()
        dict={
        "id":r.id,
        "name":r.name_text,
        "address":r.address_text
        }
        return HttpResponse(json.dumps(dict))
    elif request.method == 'GET':
        return HttpResponse("Unauthorised access to database")

@csrf_exempt
@login_required
def createnewitems(request,rest_id): 
    
    if request.method == 'POST':
        json_data=json.loads(request.body)
        rest1 = Rest.objects.filter(pk=rest_id).first()
        i = Items(dish_text=json_data.get("name1"), 
        price=json_data.get("price"),rest=rest1)
        i.save()
        return HttpResponse("Added succussfully")
    elif request.method == 'GET':
        return HttpResponse("Unauthorised access to database")
    

@csrf_exempt
@login_required
def deleterest(request,rest_id):
    
    if request.method == 'POST':
        r=Rest.objects.filter(pk=rest_id).first()
        print(r)
        r.delete()
        return HttpResponse("Restaurant Deleated")
    elif request.method =='GET':
        return HttpResponse("Unauthorised access to database")


@csrf_exempt
@login_required
def deleteitems(request,rest_id,items_id):
    
    if request.method == 'POST':
        i=Items.objects.filter(pk=items_id)
        i.delete()
        return HttpResponse("Item Deleated")
    elif request.method =='GET':
        return HttpResponse("Unauthorised access to database")

@csrf_exempt
def countR(request):
    
    return HttpResponse(Rest.objects.all().count())


@csrf_exempt
@login_required
def order(request,rest_id):
    
    if request.method == 'POST':
        rest=Rest.objects.filter(pk=rest_id).first()
        odr=Order(rest=rest,user=request.user)
        odr.save()
        print(odr)
       
        json_data = json.loads(request.body)

        for jobj in json_data:
            itm =Items.objects.filter(pk=jobj.get("id")).first()
            ord = OrderItems(order=odr,item=itm,count=jobj.get("count"))
            ord.save()
    return HttpResponse("Order Placed"+str(odr.id))


@login_required
@csrf_exempt
def order_display(request):
    
    OrderHistory=[]


    usr=request.user
    # extract the orders placed by logged in user.
    odr=Order.objects.filter(user=usr)

    # odr(list) now has all the orders placed by the loged in user. 

    for odr in odr:
        #extract the restaurant name from the restaurant id in each of odr object.
        rest=Rest.objects.filter(pk=odr.rest_id).first() 

        #extract the items from OrderItems table having order id as in odr.
        items = OrderItems.objects.filter(order_id=odr.id)

        #items is a list of dishes ordered having id equal to odr.id, each entry has item count, item_id, price.
        #now we extract the name of each items from item id we get for each item.

        itm=[]

        #itm is an array which will store objects having dish_name, price and count for all the dishes under one order.

        for items in items:
            #extracted the name of items using item_id.
            i=Items.objects.filter(pk=items.item_id).first()
            #Create object having dish_name, count and price.
            dict={
                "dish_name":i.dish_text,
                "count":items.count,
                "price":str(i.price)
            }
            itm.append(dict)
            #itm now is an list having all the items ordered from odr.id.

            #dex is an object having order_id, restaurant_name, and all the items ordered by the user in that order_id.
        dex={
            "order_id":odr.id,
            "restaurant_name":rest.name_text,
            "ordered_items":itm,
        }

        OrderHistory.append(dex)
    
    return HttpResponse(json.dumps(OrderHistory))
    





    

    


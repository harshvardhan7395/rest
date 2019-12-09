from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import HttpResponse
from .models import Rest
from .models import Items


#create new entry in restaurent table.
@csrf_exempt
def createnew(request):
    if request.method == 'POST':
        r = Rest(name_text=request.POST.get("name1"), address_text=request.POST.get("add1"))
        r.save()
        rest_list = Rest.objects.all()
        context = {'rest_list': rest_list}
        return render(request, 'resto/index.html', context)
    elif request.method == 'GET':
        return HttpResponse("Unauthorised access to database")

#renders the form for createing the restaurant entry.
def form(request):
    return render(request,'resto/form.html')

#displays the list of restaurents created.
def list(request):
        rest_list = Rest.objects.all()
        context = {'rest_list': rest_list}
        return render(request, 'resto/index.html', context)

#displays the list of items in the menu of restaurent with its name and address. The form for adding an item is also rendered.
def details(request, rest_id):
    rest1 = Rest.objects.filter(pk=rest_id).first()
    items = Items.objects.filter(rest=rest1)
    if not rest1:
        raise Http404("Restaurent does not exist")
    else:
        context = {'rest1' : rest1,'items':items}
        return render(request,'resto/details.html',context)

#creates new entry in items table and updates the dipalay with the new entry added in list.
@csrf_exempt
def createnewitems(request,rest_id): 
    if request.method == 'POST':
        rest1 = Rest.objects.filter(pk=rest_id).first()
        i = Items(dish_text=request.POST.get("name1"), price=request.POST.get("add1"),rest=rest1)
        i.save()
        items = Items.objects.filter(rest=rest1)
        context = {'items':items,'rest1':rest1}
        return render(request, 'resto/details.html', context)
    elif request.method == 'GET':
        return HttpResponse("Unauthorised access to database")


# Create your views here.

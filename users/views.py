from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

import json
# Create your views here.
@csrf_exempt
def register(request):
    if request.method =='POST':
        json_data=json.loads(request.body)
        user = User.objects.create_user(json_data.get('username'),json_data.get('email'),
        json_data.get('password'))
        user.first_name=json_data.get('first_name')
        user.last_name=json_data.get('last_name')
        user.save()
        print (user)
        return HttpResponse('User Registered')
    elif request.method =='GET':
        raise PermissionDenied()

@csrf_exempt
def log(request):
    if request.method =='POST':
        json_data = json.loads(request.body)
        user = authenticate(username=json_data.get('username'),password=json_data.get('password'))
        if not user:
            raise PermissionDenied()
        if user:
            login(request,user)
        return HttpResponse(user.is_staff)
    elif request.method =='GET':
        return HttpResponse('Access Denied')

@csrf_exempt
def logot(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponse("LOG OUT")
    elif request.method == 'GET':
        return HttpResponse('INVALID ACCESS')

from django.urls import path

from . import views

urlpatterns = [

    path('',views.list, name="list"),

    path('form/', views.form, name='form'),

    path('createnew/', views.createnew, name='createnew'),

    path('<int:rest_id>/',views.details, name='details'),

    path('<int:rest_id>/createnewitems/', views.createnewitems, name='createnewitems'),
]
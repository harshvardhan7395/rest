from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('<int:rest_id>/items/',views.details, name='details'),

    path('createnew/', views.createnew, name='createnew'),

    path('<int:rest_id>/createnewitems/',views.createnewitems, name='createnewitems'),

]
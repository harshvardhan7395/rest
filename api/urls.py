from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('<int:rest_id>/items/',views.details, name='details'),

    path('createnew/', views.createnew, name='createnew'),

    path('<int:rest_id>/createnewitems/',views.createnewitems, name='createnewitems'),

    path('<int:rest_id>/delete/',views.deleterest, name="delete"),

    path('<int:rest_id>/items/<int:items_id>/delete/',views.deleteitems,name="deleteItems"),

    path('<int:rest_id>/createorder/',views.order,name="order"),

    path('orderhistory/',views.order_display, name='order_display'),
]
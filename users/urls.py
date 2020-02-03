from django.urls import path

from . import views

urlpatterns = [
    path('register/',views.register,name="register"),

    path('login/',views.log,name="login"),

    path('logout/', views.logot,name="logout")
]

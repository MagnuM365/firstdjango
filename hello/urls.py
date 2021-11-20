from django.urls import path
from . import views

urlpatterns = [
    path("", views.alert, name="world"),
    path("vicky", views.vicky, name="vicky"),
    path("lux", views.lux, name="lux"),
    path("<str:name>", views.mixed, name="random")
]

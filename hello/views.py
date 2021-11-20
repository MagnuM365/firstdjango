from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def alert(request):
    return HttpResponse("Hello world")


def vicky(request):
    return HttpResponse("Hello, vicky")


def lux(request):
    return HttpResponse("Hello lux")


def random(request, name):
    return HttpResponse(f"hello, {name.capitalize()}")


def mixed(request, name):
    return render(request, "hello/djang.html", {
        "name": name
    })

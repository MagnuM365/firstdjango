from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls.base import reverse

# Create your views here.
tasks = []


class Tasktoadd(forms.Form):
    task = forms.CharField(label="New Task")


def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })


def add(request):
    if request.method == "POST":
        form = Tasktoadd(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": Tasktoadd()
    })

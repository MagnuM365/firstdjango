from django.shortcuts import render
import datetime
# Create your views here.


def check(request):
    now = datetime.datetime.now()
    return render(request, "holiday/check.html", {
        "birthday": now.month == 11 and now.day == 12
    })

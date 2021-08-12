from django.shortcuts import redirect, render
from gateau.models import Dessert, Cafe, Video, Recipe
from django.http import HttpRequest, HttpResponse


def dessert_list(request):
    qs = Dessert.objects.all()
    return render(
        request,
        "gateau/dessert_list.html",
        {
            "dessert_list": qs,
        },
    )

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse


def index(request):
    return render(request, "core/index.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "core/about.html")

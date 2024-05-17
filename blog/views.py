from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    HttpResponsePermanentRedirect,
    HttpResponseNotFound,
    HttpResponseBadRequest,
    HttpResponseForbidden,
)
from django.template.response import TemplateResponse
from django.shortcuts import render


def index(request):
    langs = ['Python', 'Java', 'C', 'C++', 'Go', 'Javascript', 'PHP']
    # render(request, template, context)
    return render(request, 'blog/index.html', context={'langs': langs})


def access(request, age):
    # if age beyond range below or not valid value
    if age not in range(1, 111):
        return HttpResponseBadRequest("Invalid data")
    # if age more than 17
    if age > 17:
        return HttpResponse("Access allowed")
    # otherwise, or when age less than or equals 17
    return HttpResponseForbidden("Access denied: age is not enough!")


def about(request):
    return HttpResponse("About")


def contact(request):
    return HttpResponseRedirect("/about")  # temporary redirect with status code 302


def details(request):
    return HttpResponsePermanentRedirect("/")  # permanent redirect with status code 301


def user(request):
    age = request.GET.get("age", 0)
    name = request.GET.get("name", "Undefined")
    return HttpResponse(f"<h2>Name: {name}, Age: {age}")


def products(request):
    return HttpResponse("Products list")


def new(request):
    return HttpResponse("New products")


def top(request):
    return HttpResponse("Popular products")
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


def index(request):
    return HttpResponse("<h2>Main page</h2>")


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
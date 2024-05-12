from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Main</h2>")


def about(request):
    return HttpResponse("<h2>About website</h2>")


def contact(request):
    return HttpResponse("<h2>Contacts</h2>")
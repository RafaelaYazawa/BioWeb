from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . models import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def list(request):
    search = request.GET.get("query")
    if search:
        people = Person.objects.filter(name__contains=search)
    else:
        people = Person.objects.all()

    context = {
        "people": people,
        "search": search
    }
    return render(request, "lists.html", context=context)

def details(request, id):
    person = get_object_or_404(Person, pk=id)
    context = {
        "person": person
    }
    return render(request, "biography.html", context=context)
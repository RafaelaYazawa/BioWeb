from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def list(request):
    search = request.GET.get("query")
    if search:
        people = Person.objects.filter(biography__contains=search)
    else:
        people = Person.objects.all()

    context = {
        "people": people
    }
    return render(request, "lists.html", context=context)
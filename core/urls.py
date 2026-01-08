from django.urls import path
from .  import views

urlpatterns = [
    path("", views.index, name="index"),
    path("biographies", views.list, name="biographies"),
    path("bio/<int:id>", views.details, name="bio")
]
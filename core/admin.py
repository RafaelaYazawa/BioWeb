from django.contrib import admin
from . models import *

class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "modified_at"]
    search_fields = ["name"]
# Register your models here.
admin.site.register(Person, PersonAdmin)
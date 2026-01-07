from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    biography = models.TextField()
    url_photo = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Response(models.Model) :
    name = models.CharField(max_length=40, default="", blank=False)
    testimony = models.TextField(max_length=2000, default="", blank=False)

    def __str__ (self):
        return (self.name)
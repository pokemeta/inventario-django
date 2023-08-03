from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=250,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
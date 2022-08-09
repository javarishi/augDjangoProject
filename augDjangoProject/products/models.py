from django.db import models

# Create your models here.
class Course(models.Model):
    
    name = models.CharField(null=False, blank=False, max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.CharField(max_length=3)
    reviews = models.TextField()
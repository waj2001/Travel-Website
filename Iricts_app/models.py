from django.db import models


# Create your models here.

class employee(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=150)
    image = models.ImageField(upload_to="emp_photo") 

    def __str__(self):
        return self.name

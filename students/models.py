

from django.db import models

# Create your models here.

from django.utils import timezone
 

class Students(models.Model):
 
    firstName = models.CharField(max_length=50)
    lastName =  models.CharField(max_length=50)
    #birthDate = models.DateTimeFields(default=timezone.now)
    adress = models.CharField(max_length=50)
    desciption = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
 

    def __str__(self):
        return self.firstName


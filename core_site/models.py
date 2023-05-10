from django.db import models

# Create your models here.


class Records(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=50) 
    lastname = models.CharField(max_length=50) 
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    city =  models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=15)

    def __self__(self):
        return (f"{self.firstname} {self.lastname}")

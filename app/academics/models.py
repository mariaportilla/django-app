from django.db import models
import datetime

# Create your models here.
#model.DataTimeField(auto_now=True, null=false)=> updates_at
#model.DataTimeField(auto_now_add=True, null=false)=> Desfault now()

class User(models.Model):
    
    email=models.EmailField(null=True, blank=True)
    password= models.CharField(null=True, blank=True)
    status=models.BooleanField(null=True, blank=True, default=True)
    created_at= models.DateTimeField(default=datetime.datetime.now())
    updated_at= models.DateTimeField(default=datetime.datetime.now())
    delete_at= models.DateTimeField(null=True, blank=True)

class Person(models.Model):
    firstname = models.CharField(max_length =20)
    lastname = models.CharField(max_length=20)
    age = models.CharField()
    ident_number = models.CharField(max_length= 12, blank=True)
    created_at= models.DateTimeField(default=datetime.datetime.now())
    updated_at= models.DateTimeField(default=datetime.datetime.now())
    delete_at= models.DateTimeField(null=True, blank=True)
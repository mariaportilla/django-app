from django.db import models
import datetime

# Create your models here.
#model.DataTimeField(auto_now=True, null=false)=> updates_at
#model.DataTimeField(auto_now_add=True, null=false)=> Desfault now()

class User(models.Model):
    
    email=models.EmailField(null=False, blank=False)
    password= models.CharField(null=False, blank=False)
    status=models.BooleanField(null=True, blank=True, default=True)
    created_at= models.DateTimeField(default=datetime.datetime.now(), null=False, blank=False)
    updated_at= models.DateTimeField(default=datetime.datetime.now(),null=False, blank=False)
    delete_at= models.DateTimeField(null=True, blank=True)

class Person(models.Model):
    firstname = models.CharField(max_length =50, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=False, blank=False)
    id_ident_type = models.IntegerField(null= False, blank=False)
    ident_number = models.CharField(max_length= 15, null= False, blank=True)
    id_exp_city = models.IntegerField(null= False, blank=False)
    address = models.CharField(max_length=150, null=False,blank= False)
    mobile = models.CharField(max_length =50,null= False, blank=False)
    id_user = models.IntegerField(null= False, blank=False)
    created_at= models.DateTimeField(default=datetime.datetime.now(),null= False, blank=False)
    updated_at= models.DateTimeField(default=datetime.datetime.now(),null= False, blank=False)
    delete_at= models.DateTimeField(null=True, blank=True)

class Students(models.Model):
    code = models.CharField(max_length= 50, null= False, blank=False)
    id_person = models.IntegerField(null= False, blank=False)
    status=models.BooleanField(null=True, blank=True, default=True)
    created_at= models.DateTimeField(default=datetime.datetime.now(),null= False, blank=False)
    updated_at= models.DateTimeField(default=datetime.datetime.now(),null= False, blank=False)
    delete_at= models.DateTimeField(null=True, blank=True)

class Identification(models.Model):
    name = models.CharField(max_length =50,null= False, blank=False)
    abrev = models.CharField(max_length=10,null= False, blank=False)
    descrip = models.CharField(max_length=100,null= False, blank=False)
    created_at= models.DateTimeField(default=datetime.datetime.now(),null= False, blank=False)
    updated_at= models.DateTimeField(default=datetime.datetime.now(),null= False, blank=False)
    delete_at= models.DateTimeField(null=True, blank=True)

class Cities(models.Model):
    name = models.CharField(max_length =100,null= False, blank=False)
    abrev = models.CharField(max_length=10,null= False, blank=False)
    descrip = models.CharField(max_length=10,null= False, blank=False)
    id_dept = models.IntegerField(null= True, blank=False)
    created_at= models.DateTimeField(default=datetime.datetime.now(),null= False, blank=False)
    updated_at= models.DateTimeField(default=datetime.datetime.now(),null= False, blank=False)
    delete_at= models.DateTimeField(null=True, blank=True)

class Departaments(models.Model):
    name = models.CharField(max_length =100,null= False, blank=False)
    abrev = models.CharField(max_length=10,null= False, blank=False)
    descrip = models.CharField(max_length=10,null= False, blank=False)
    id_dept = models.IntegerField(null= False, blank=False)
    created_at= models.DateTimeField(default=datetime.datetime.now(),null= False, blank=False)
    updated_at= models.DateTimeField(default=datetime.datetime.now(),null= False, blank=False)
    delete_at= models.DateTimeField(null=True, blank=True)

class Contries(models.Model):
    name = models.CharField(max_length =100,null= False, blank=False)
    abrev = models.CharField(max_length=10,null= False, blank=False)
    descrip = models.CharField(max_length=10,null= False, blank=False)
    created_at= models.DateTimeField(default=datetime.datetime.now(),null= False, blank=False)
    updated_at= models.DateTimeField(default=datetime.datetime.now(),null= False, blank=False)
    delete_at= models.DateTimeField(null=True, blank=True)

from django.db import models
class ModelNikita(models.Model):
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=10)
    name = models.CharField(max_length=10)

# Create your models here.
class Img(models.Model):
   Image = models.ImageField(upload_to='images')
   title = models.CharField(max_length=30)

class Img_foto(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='acs/static/imgs')

class ModelReg(models.Model):
   login = models.CharField(max_length=30)
   password= models.CharField(max_length=30)
   email = models.CharField(max_length=30)




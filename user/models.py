from django.db import models

# Create your models here.
class register(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100,primary_key=True)
    mobile=models.CharField(max_length=30)
    ppic=models.ImageField(upload_to='static/profile',null=True)
    passwd=models.CharField(max_length=60)
    cpasswd=models.CharField(max_length=60)
    address=models.TextField()
class category(models.Model):
    Name=models.CharField(max_length=40)
class worker(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    aadhar=models.CharField(max_length=60)
    pan=models.CharField(max_length=60)
    phone=models.CharField(max_length=60)
    aphone=models.CharField(max_length=60)
    pic=models.ImageField(upload_to='static/worker',null=True)
    job=models.CharField(max_length=60)
    date=models.DateField()
    city=models.CharField(max_length=50)
class userdata(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=15)
    amobile=models.CharField(max_length=15)
    city=models.CharField(max_length=40)
    address=models.TextField()
    job=models.CharField(max_length=40)

class mcart(models.Model):
    userid=models.CharField(max_length=70)
    pid=models.IntegerField()
    cdate=models.DateField()
    status=models.BooleanField()
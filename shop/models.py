from django.db import models
from django.utils.timezone import datetime
# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstname= models.CharField('First Name', max_length=100)
    lastname= models.CharField('Last Name', max_length=100)
    username= models.CharField('User Name', max_length=100)
    
    email= models.CharField('User email', max_length=100, unique=True)
    password = models.CharField('User password', max_length=100)
    passwordd = models.CharField('User passwordd', max_length=100)
 
	# password= models.CharField('User password', max_length=100)
    # form_id = models.AutoField(primary_key=True)

 
 
    timeStamp = models.DateField(blank=True)
    def __str__(self):
        return self.username


class Contact(models.Model):
    form_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=5000, default="")
    timeStamp = models.DateField(blank=True)

    

    def __str__(self):
        return str(self.form_id)+") "+ "Name is:- "+self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="")
    cnic = models.CharField(max_length=13, default="")
    address = models.CharField(max_length=50, default="")
    addresss = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    number = models.CharField(max_length=12, default="")
    country = models.CharField(max_length=10,default="")
    city = models.CharField(max_length=10,default="")
    item1 = models.CharField(max_length=50,default="")
    item2 = models.CharField(max_length=50,default="")
    item3 = models.CharField(max_length=50,default="")
    item4 = models.CharField(max_length=50,default="")
    item5 = models.CharField(max_length=50,default="")
    item6 = models.CharField(max_length=50,default="")
    item7 = models.CharField(max_length=50,default="")
    item8 = models.CharField(max_length=50,default="")
    quantity1= models.CharField(max_length=50,default="")
    quantity2= models.CharField(max_length=50,default="")
    quantity3= models.CharField(max_length=50,default="")
    quantity4= models.CharField(max_length=50,default="")
    quantity5= models.CharField(max_length=50,default="")
    quantity6= models.CharField(max_length=50,default="")
    quantity7= models.CharField(max_length=50,default="")
    quantity8= models.CharField(max_length=50,default="")
    total = models.IntegerField()
    timeStamp = models.DateField(blank=True)
# models.DateField(_(""), auto_now=False, auto_now_add=False)
    def __str__(self):
        return str(self.order_id)+") "+ "Name is:- "+self.name
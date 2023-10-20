from django.db import models

# Create your models here.

class regmod1(models.Model):
    fname=models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    uname = models.CharField(max_length=30)
    num=models.IntegerField()
    em=models.EmailField()
    im=models.FileField(upload_to='bank_app/static')
    pin=models.CharField(max_length=30) #int(pin) views il vilikkanam
    balance=models.IntegerField()
    ac_num=models.IntegerField()
    def __str__(self):
        return self.fname

class logmod1(models.Model):
    uname=models.CharField(max_length=30)
    pswd=models.CharField(max_length=30)
    # def __str__(self):
    #     return self.uname


class addamount(models.Model):
    uid = models.IntegerField()

    amount=models.IntegerField()  #
    date=models.DateField(auto_now_add=True) #to add automatically

class withdrawamount(models.Model):
    uid=models.IntegerField()

    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)

class ministatement(models.Model):
    choice=[
        ('withdraw','withdraw'),
        ('deposit','deposit'),
    ]
    statement=models.IntegerField(choices=choice)

class newsmodel(models.Model):
    topic=models.CharField(max_length=30)
    content = models.CharField(max_length=3000)
    date=models.DateField(auto_now_add=True)


class tablesmod(models.Model):
    uid = models.IntegerField()
    name=models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    number = models.CharField(max_length=30)



class wishlist(models.Model):
    uid = models.IntegerField()
    newsid=models.IntegerField()
    topic = models.CharField(max_length=30)
    content = models.CharField(max_length=3000)
    date = models.DateField()

import datetime
from django.db import models

# class place(models.Model):
#     name=models.CharField(max_length=255)
#     img=models.ImageField(upload_to='pics')
#     desc=models.TextField()
    
#     def __str__(self):
#         return self.name
# class photo(models.Model):
#     names=models.CharField(max_length=255)
#     imgs=models.ImageField(upload_to='picture')
#     descs=models.TextField()
    
# def __str__(self):
#         return self.names
class Department(models.Model):
    name = models.CharField(max_length=100)
    class meta:
        db_table="Department"

class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Order(models.Model):
    user_id= models.IntegerField(default=1)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField(default=datetime.date.today)
    age = models.IntegerField(default=18)
    gender= models.CharField(max_length=100,default='null')
    phn=models.IntegerField(default=1234567890)
    email=models.EmailField(default='null')
    add = models.CharField(max_length=255, default='null')
    depart= models.CharField(max_length=100,default='null')
    course= models.CharField(max_length=100,default='null')
    purpose= models.CharField(max_length=100,default='null')
    material= models.CharField(max_length=100,default='null')
    def __str__(self):
        return self.name
    


# Create your models here.

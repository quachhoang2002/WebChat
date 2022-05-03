import email
from pyexpat import model
from tkinter import CASCADE
from turtle import update
from unicodedata import name
from venv import create
from django.db import models
from django.contrib.auth.models import User
from numpy import str_

# Create your models here.
class Topic(models.Model):
    name=models.CharField(max_length=50)
 
    def __str__(self):
         return self.name
        


class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True )
    name=models.CharField(max_length=50)
    description=models.TextField(null=True,blank=True)
    update=models.DateTimeField(auto_now=True)
    #participants=
    created=models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        ordering = ['-update' , '-created']
        
    def __str__(self):
        return self.name
    

class Message(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    body = models.TextField()
    update=models.DateTimeField(auto_now=True)
    create=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.body[0:50]
    
    

from curses import REPORT_MOUSE_POSITION
from multiprocessing import context
from pydoc_data.topics import topics
from re import I
from unicodedata import name
from urllib import request
from urllib.request import Request
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponseRedirect
from .models import Room, Topic
from .forms import RoomForm,CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here. 
# rooms=[
#     {'id':1,'name':'HoangDepTrai' },
#     {'id':2,'name':'HoangVipPro' },
#     {'id':3,'name':'HoangNe' }   
# ]

def index(request):
    q=request.GET.get('q') if request.GET.get('q') != None  else ''  

    rooms=Room.objects.filter(Q(topic__name__icontains=q)|
                              Q(name__icontains=q)|
                              Q(description__icontains=q)
                              )
    
    topics=Topic.objects.all()
    
    context={'rooms':rooms,'topics':topics}
    return render(request,'pages/index.html',context)


def room(request,pk):
    room=Room.objects.get(id=pk)
    context={'room':room}
    return render(request,'pages/room.html',context)

@login_required(login_url='home:login_form')   
def createRoom(request):
    form=RoomForm()
    if request.method == 'POST':
          form = RoomForm(request.POST)
          if form.is_valid() :
              form.save()
              return redirect('home:index')
    context={'form':form}
    return render(request,'pages/room_form.html',context)
 
@login_required(login_url='home:login_form')      
def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    
    if request.user != room.host:
        return HttpResponse('ban khong co quyen tury cap ')
    
    if request.method=='POST':
        form=RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    context={'form':form}
    return render(request,'pages/room_form.html',context)

def delelteRoom(request,pk):
    room=Room.objects.get(id=pk) 
    if request.method=='POST':
        room.delete()
        return redirect('home:index')
    return render(request,'pages/delete.html',{'obj':room})

def registerUser(request):  
    page='register'
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
             form.save()
             user=form.cleaned_data.get('username')
             messages.success(request,'Tao Thanh Cong'+user)
        else:
            messages.error(request,'Co loi')
    context={'form':form,'page':page}
    return render(request,'pages/login-register-form.html',context)      

def Login(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home:index')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'tai khoan khong ton tai ')  
        user=authenticate(request , username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            messages.error(request,'sai tai khoan hoac mat khau ')
    context={'page':page}
    return render(request,'pages/login-register-form.html',context)

def Logout(request):
    logout(request)
    return redirect('home:index')
    

      


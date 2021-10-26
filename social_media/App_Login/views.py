
from django import forms
from django.contrib.auth.models import User
from django.http import response
from django.shortcuts import render,HttpResponseRedirect

from App_Login.forms import CreateNewUser,Editprofile
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse,reverse_lazy
from App_Login.models import userprofile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from code_main.forms import postfrom
from App_Login.models import follow as follow2


def singup(request):
    form=CreateNewUser()
    registered=False
    if request.method=='POST':
        form=CreateNewUser(data=request.POST)
        if form.is_valid():
            user=form.save()
            registered=True
            user_profile=userprofile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('login'))


    return render(request,'applog/sing_up.html',context={'title':'singup Inragram','form':form})        



def login_page(request):
    form=AuthenticationForm()
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))


    return render(request,'applog/login.html',context={'title':'login','form':form})            


@login_required
def edit_profile(request):
    current_user=userprofile.objects.get(user=request.user)
    form=Editprofile(instance=current_user)
    if request.method=="POST":
        form=Editprofile(request.POST,request.FILES,instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form=Editprofile(instance=current_user)
            return HttpResponseRedirect(reverse('profile'))


    return render(request,'applog/profile.html',context={'title':'edit profile','form':form})

@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))



@login_required
def profile(request):
    form=postfrom()
    if request.method=="POST":
        form=postfrom(request.POST,request.FILES)
        if form.is_valid():
            post= form.save(commit=False)
            post.author=request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
    return render (request,'applog/user.html',context={'title':'user','form':form})


@login_required
def user(request,username):
    user_other=User.objects.get(username=username)
    already_followed =follow2.objects.filter(follower=request.user,following=user_other) 

    if user_other == request.user:
        return HttpResponseRedirect(reverse('profile'))

    return render(request,'applog/user_other.html',context={'user_other':user_other,'already_followed':already_followed})

@login_required
def follow(request,username):
    following_user=User.objects.get(username=username)
    follower_user=request.user
    already_followed=follow2.objects.filter(follower=follower_user,following=following_user)
    if not already_followed:
        followed_user=follow2(follower=follower_user,following=following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('user',kwargs={'username':username}))

@login_required
def unfollow(request,username):
    following_user=User.objects.get(username=username)
    follower_user=request.user
    already_followed=follow2.objects.filter(follower=follower_user,following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('user',kwargs={'username':username}))

 


    
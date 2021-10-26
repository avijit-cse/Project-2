from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from App_Login.models import userprofile
from django.contrib.auth.models import User

from App_Login.models import follow
from code_main.models import post,like
from django.urls import reverse









#@login_required
def index(request):

    following_list=follow.objects.filter(follower=request.user)
    posts=post.objects.filter(author__in=following_list.values_list('following'))
    liked_post=like.objects.filter(user=request.user)
    liked_post_list=liked_post.values_list('post',flat=True)
    print(liked_post_list)
    if request.method=="GET":
        search=request.GET.get('search','')
        result=User.objects.filter(username__icontains=search)


    return render(request,'codemain/home.html',context={'title':'home page','search':search,'result':result,'posts':posts,'liked_post_list':liked_post_list})

@login_required
def likes(request,pk):
    posts=post.objects.get(pk=pk)
    already_liked=like.objects.filter(post=posts,user=request.user)
    if not already_liked:
        liked_post=like(post=posts,user=request.user)
        liked_post.save()
    return HttpResponseRedirect(reverse('home'))

@login_required
def unlikes(request,pk):
    posts=post.objects.get(pk=pk)
    liked_post=like.objects.filter(post=posts,user=request.user)
    liked_post.delete()
    return HttpResponseRedirect(reverse('home'))




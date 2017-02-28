from django.shortcuts import render
from hackathon.models import Post
# Create your views here.
def welcome(request):
    return render(request,'hackathon/welcome.html',{})
def post_list(request):
    posts=Post.objects.all()
    content={
        'posts':posts,
    }
    return render(request,'hackathon/post_list.html',content)

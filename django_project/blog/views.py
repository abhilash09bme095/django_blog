from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts = [
    {
        'author': 'coryMS',
        'title': 'Blogpost 1',
        'content': 'first post content',
        'date_posted': 'Aug 27 2019',
    },
    {
        'author': 'Abhi',
        'title': 'Blogpost 2',
        'content': 'Second post content',
        'date_posted': 'Aug 31 2019',
    }

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})








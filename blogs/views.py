from django.shortcuts import render

from .models import BlogPost

# Create your views here.
def index(request):
    """Index page showin all posts in order of adding(newest on top)"""

    posts = BlogPost.objects.all()
    posts = posts.order_by('-date_added')
    context = {'posts' : posts}
    return render(request, 'blogs/index.html', context)

def post(request, post_id):
    """Page for post(for comments, editing etc)"""

    post = BlogPost.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blogs/post.html', context)

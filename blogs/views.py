from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost
from .forms import BlogPostForm

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

def new_post(request):
    """Create new post"""

    #GET = no data, create a blank;
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        #POST
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

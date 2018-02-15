from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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
    context = {'post': post }
    return render(request, 'blogs/post.html', context)

@login_required
def new_post(request):
    """Create new post"""

    #GET = no data, create a blank;
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        #POST
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request,post_id):
    """Edit exisiting post"""

    post = BlogPost.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404
    #if GET, render post
    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            if 'save' in request.POST:
                form.save()
                return HttpResponseRedirect(reverse('blogs:post', args=[post.id]))
            if 'delete' in request.POST:
                post.delete()
                return HttpResponseRedirect(reverse('blogs:index'))

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

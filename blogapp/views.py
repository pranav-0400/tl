from django.shortcuts import render
from .models import Blog_Post
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    posts = Blog_Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def blog_detailView(request, slug):
    post = Blog_Post.objects.get(slug = slug)
    comments = post.comments.all()
    new_comment = None
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('blog_detail', args = [str(post.slug)]))
            
    else:
        form = CommentForm()
    

    return render(request, 'blog_detail.html', {'post': post,
    'form': form, 'comments':comments, 'new_comment':new_comment})
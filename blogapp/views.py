from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from django.utils import timezone
from .forms import CommentForm
from .forms import BlogPost

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html',{'blogs':blogs})

def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def delete(request, blog_id):
    blog_detail=get_object_or_404(Blog, pk=blog_id)
    blog_detail.delete()
    return redirect('home')

def edit(request, blog_id):
    if(request.method == 'POST'):
        blog_detail=get_object_or_404(Blog, pk=blog_id)
        return render(request, 'edit.html',{'blog':blog_detail})

def update(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    if(request.method=="POST"):
        blog.title=request.POST['title']
        blog.body=request.POST['body']
        blog.save()
        return redirect('/blog/'+str(blog.id))

def add_comment(request,blog_id):
        blog=get_object_or_404(Blog,pk=blog_id)
        if request.method=='POST':
                form=CommentForm(request.POST)
                if form.is_valid():
                        comment=form.save(commit=False)
                        comment.blog=blog
                        comment.save()
                        return redirect('/blog/'+str(blog.id))
        else:
                form=CommentForm()
                return render(request,'add_comment.html',{'form':form})

def blogpost(request):
        if request.method=='POST':
                form=BlogPost(request.POST)
                if form.is_valid():
                        post=form.save(commit=False)
                        post.pub_date=timezone.now()
                        post.save()
                        return redirect('home')
        else:
                form=BlogPost()
                return render(request,'new.html',{'form':form})


def delete_comment(request,comment_id):
        comment=get_object_or_404(Comment, pk=comment.id)
        comment.delete()
        return redirect('home')

def edit_comment(request,comment_id):
        comment=get_object_or_404(Comment, pk=comment.id)
        if request.method=='POST':
                form = CommentForm(request.POST, instance=comment)
                if form.is_valid():
                        comment=form.save(commit=False)
                        comment.save()
                        return redirect('home')
                else:
                        form=CommentForm(instance=comment)
                        return render(request, 'add_comment.html', {'form':form})

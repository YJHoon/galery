from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Galery
from .forms import PostForm, CommentForm, GaleryForm
from django.contrib.auth.models import User
import pdb

#galery

def new_galery(request):
    return render(request, 'posts/new_galery.html')

def create_galery(request):
    form = GaleryForm()
    if request.method == "POST":
        form = GaleryForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False) # form을 당장 저장하지 않음. 데이터 저장 전 뭔가 하고 싶을 때 사용.
            form.user = request.user #request 날리때의 유저를 뜻함
            form.save()
            return redirect('home')
    return render(request, 'posts/create_galery.html', {'form': form})

def show_galery(request, id):
    galery = get_object_or_404(Galery, pk=id)
    return render(request, 'posts/show_galery.html', {"galery": galery})
    
def update_galery(request, id):
    galery = get_object_or_404(Galery, pk=id)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        galery.title = title
        galery.content = content
        galery.save()
        return redirect('posts:show_galery', galery.id)
    return render(request, 'posts/update_galery.html', {"galery": galery})
    
def delete_galery(request, id):
    galery = get_object_or_404(Galery, pk=id)
    galery.delete()
    return redirect('home')
    



#post

def new(request, id):
    galery = get_object_or_404(Galery, pk=id)
    return render(request, 'posts/new.html', {"galery": galery})


def create(request, id):
    form = PostForm()
    galery = get_object_or_404(Galery, pk = id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # form = form.save(commit=False) # form을 당장 저장하지 않음. 데이터 저장 전 뭔가 하고 싶을 때 사용.
            # form.user = request.user #request 날리때의 유저를 뜻함
            # form.save()
            post = form.save(commit=False) # form을 당장 저장하지 않음. 데이터 저장 전 뭔가 하고 싶을 때 사용.
            post.galery = galery
            post.user = request.user #request 날리때의 유저를 뜻함
            post.save()
            return redirect('posts:show_galery', galery.id)
    return render(request, 'posts/create.html', {'form': form})

def show(request, id):
    # galery = get_object_or_404(Galery, pk=id)
    # return render(request, 'posts/show.html', {"galery":galery})
    post = get_object_or_404(Post, pk=id)
    # post = galery.posts
    return render(request, 'posts/show.html', {"post":post})
    
def update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post.title = title
        post.content = content
        post.save()
        return redirect('posts:show', post.id)
    return render(request, 'posts/update.html', {"post": post})

def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('posts:show_galery')
    
    
def like(request, id):
    user = request.user
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        if post.like.filter(id = user.id).exists():
            post.like.remove(user)
        else:
            post.like.add(user)
    return redirect('posts:show', post.id)

    
    
#comment    

def new_comment(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/new_comment.html', {'post': post})

def create_comment(request, id):
    form = CommentForm()
    post = get_object_or_404(Post,pk = id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('posts:show', post.id)
    return render(request, 'posts/new_comment.html', {'form': form})
    
def delete_comment(request,id):
    comment = get_object_or_404(Comment, pk=id)
    post = comment.post
    comment.delete()
    return redirect('posts:show', post.id)
    
def update_comment(request, id):
    comment = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        content = request.POST.get('content')
        comment.content = content
        comment.save()
        return redirect('posts:show', comment.id)
    return render(request, 'posts/update_comment.html', {"comment": comment})
    


def like_comment(request, id):
    user = request.user
    comment = get_object_or_404(Comment, pk=id)
    if request.method == "POST":
        if comment.like.filter(id = user.id).exists():
            comment.like.remove(user)
        else:
            comment.like.add(user)
    return redirect('posts:show', comment.id)
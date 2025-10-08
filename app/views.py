from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from app.forms import PostForm
from app.models import Post
# Create your views here.
def inicio(req):
    posts = Post.objects.filter(aprovado = True)
    return render(req, 'filho.html',{
        'posts': posts
    })

def controle(req):
    lista = [1, 2, 6, 'teste', 10]
    hoje = datetime.now()
    return render(req, 'controle.html', {
        'variavel': lista,
        'agora': hoje
    })

from django.shortcuts import redirect, render
from .forms import PostForm
from . import models

@login_required(login_url='/contas/login')
def postar_view(request:HttpRequest):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post:Post = form.save(commit = False)
            post.autor = request.user
            if request.user.is_staff:
                post.aprovado = True
            post.save()
            return redirect("lista_posts")
    else:
        form = PostForm()

    return render(request, "postar.html", {"form": form})

def lista_posts(req):
    posts = models.Post.objects.filter(aprovado = True).all()
    return render(req, "lista_posts.html", {"posts": posts})

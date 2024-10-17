from django.shortcuts import render

from .models import Post
from .models import Combo

def frontpage(request):
    posts = Post.objects.all()
    return render(request,"app/frontpage.html", {"posts": posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "app/post_detail.html", {"post": post})

def character_page(request, character_name):
    combos = Combo.objects.filter(character=character_name)
    return render(request, f'app/Character-Page/{character_name}.html', {'combos': combos})
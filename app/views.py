from django.shortcuts import render, get_object_or_404

from .models import Post
from .models import Post, Combo, Character

def frontpage(request):
    posts = Post.objects.all()
    characters = Character.objects.all()
    return render(request, "app/frontpage.html", {"posts": posts, "characters": characters})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "app/post_detail.html", {"post": post})

def character_detail(request, name):
    characters = Character.objects.all()
    character = get_object_or_404(Character, name=name)
    combos = Combo.objects.filter(character=character)
    return render(request, "app/character_detail.html", {'characters': characters,'character': character, 'combos': combos})
from django.shortcuts import render, get_object_or_404
from .models import Post, Combo, Character
from django.db.models import Q

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

    # フィルターおよび検索パラメータを取得
    difficulty = request.GET.get('difficulty')
    okizeme = request.GET.get('okizeme')
    search_query = request.GET.get('search')
    input_type = request.GET.get('input_type')

    combos = Combo.objects.filter(character=character)

    # 難易度フィルター
    if difficulty:
        combos = combos.filter(difficulty=difficulty)
    
    # 起き攻めフィルター
    if okizeme:
        combos = combos.filter(okizeme=(okizeme == 'True'))

    # 操作タイプでフィルター
    if input_type:
        combos = combos.filter(input_type=input_type)
    
    # 検索フィルター
    if search_query:
        combos = combos.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    

    return render(request, "app/character_detail.html", {
        'characters': characters,
        'character': character, 
        'combos': combos,
        "difficulty": difficulty,
        "okizeme": okizeme,
        "search_query": search_query,
        "input_type": input_type
        })
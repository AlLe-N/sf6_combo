from django.shortcuts import render, get_object_or_404
from .models import Post, Combo, Character
from django.db.models import Q
from django.core.paginator import Paginator

def frontpage(request):
    posts = Post.objects.all()
    characters = Character.objects.all()
    return render(request, "app/frontpage.html", {"posts": posts, "characters": characters})

def character_detail(request, name):
    characters = Character.objects.all()
    character = get_object_or_404(Character, name=name)

    # フィルターおよび検索パラメータを取得
    difficulty = request.GET.get('difficulty')
    okizeme = request.GET.get('okizeme')
    search_query = request.GET.get('search')
    input_type = request.GET.get('input_type')
    hit_situation = request.GET.get('hit_situation')

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

    # ヒット状況でフィルター
    if hit_situation:
        combos = combos.filter(hit_situation=hit_situation)

    # 検索フィルター
    if search_query:
        combos = combos.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

    # ページネーション設定（1ページに10件表示）
    paginator = Paginator(combos, 10)
    page_number = request.GET.get('page')  # `?page=2` などの値を取得
    combos = paginator.get_page(page_number)

    return render(request, "app/character_detail.html", {
        'characters': characters,
        'character': character, 
        'combos': combos,
        "difficulty": difficulty,
        "okizeme": okizeme,
        "search_query": search_query,
        "input_type": input_type,
        "hit_situation": hit_situation
    })

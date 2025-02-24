from django.shortcuts import render, get_object_or_404
from .models import Post, Combo, CHARACTER_CHOICES, Character
from django.db.models import Q
from django.core.paginator import Paginator

CHARACTER_DETAILS = {
    "ryu": {"description": "リュウは波動拳・昇龍拳・竜巻旋風脚を持つオールラウンダー"},
    "ken": {"description": "ケンは攻撃的なスタイルで豪快なコンボが得意"},
    "juri": {"description": "ジュリは風破ストックシステムを持ち、多彩な蹴り技で攻める"},
    "blanka": {
            "description": 
            """電気：214P 
            バチカ：2溜め8K
            ロリ：4溜め6P
            エアロリ：空中4溜め6P
            バクロリ：63214K
            人形設置：22P
            コマ投げ：236P
            リフト：2PP+P
            レイドジャンプ：2PP+K
            サプフォ：KKK"""
            },
    }

def frontpage(request):
    posts = Post.objects.all()
    character_choices = CHARACTER_CHOICES
    return render(request, "app/frontpage.html", {"posts": posts, 'character_choices': character_choices})

def character_detail(request, character_name):
    character = character_name
    character_choices = CHARACTER_CHOICES
    character_info = CHARACTER_DETAILS.get(character_name, {"description": "このキャラクターの詳細は準備中です。"})
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

    # ページネーション設定
    paginator = Paginator(combos, 10)
    page_number = request.GET.get('page')
    combos = paginator.get_page(page_number)

    return render(request, "app/character_detail.html", {
        'character_choices': character_choices,
        'character': character, 
        'character_info': character_info,
        'combos': combos,
        "difficulty": difficulty,
        "okizeme": okizeme,
        "search_query": search_query,
        "input_type": input_type,
        "hit_situation": hit_situation
    })

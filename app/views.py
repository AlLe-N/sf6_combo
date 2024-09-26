from django.shortcuts import render

from .models import Post

def frontpage(request):
    posts = Post.objects.all()
    return render(request,"app/frontpage.html", {"posts": posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "app/post_detail.html", {"post": post})

def Luke_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Luke.html",{"posts": posts})

def Jamie_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Jamie.html",{"posts": posts})

def Manon_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Manon.html",{"posts": posts})

def Kimbery_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Kimbery.html",{"posts": posts})

def Marisa_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Marisa.html",{"posts": posts})

def Lily_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Lily.html",{"posts": posts})

def Jp_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Jp.html",{"posts": posts})

def Juri_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Juri.html",{"posts": posts})

def Dj_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Dj.html",{"posts": posts})

def Cammy_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Cammy.html",{"posts": posts})

def Ryu_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Ryu.html",{"posts": posts})

def Honda_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Honda.html",{"posts": posts})

def Blanka_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Blanka.html",{"posts": posts})

def Guile_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Guile.html",{"posts": posts})

def Ken_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Ken.html",{"posts": posts})

def Chunli_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Chunli.html",{"posts": posts})

def Zangief_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Zangief.html",{"posts": posts})

def Dhalsim_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Dhalsim.html",{"posts": posts})

def Rashid_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Rashid.html",{"posts": posts})

def Aki_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Aki.html",{"posts": posts})

def Ed_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Ed.html",{"posts": posts})

def Gouki_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Gouki.html",{"posts": posts})

def Vega_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Vega.html",{"posts": posts})

def Terry_view(request):
    posts = Post.objects.all()
    return render(request,"app/Character-Page/Terry.html",{"posts": posts})
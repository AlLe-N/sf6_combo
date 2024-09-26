"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views import frontpage, post_detail,Luke_view,Jamie_view,Manon_view,Kimbery_view,Marisa_view,Lily_view,Jp_view,Juri_view,Dj_view,Cammy_view,Ryu_view,Honda_view,Blanka_view,Guile_view,Ken_view,Chunli_view,Zangief_view,Dhalsim_view,Rashid_view,Aki_view,Ed_view,Gouki_view,Vega_view,Terry_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",frontpage,name="frontpage"),
    path('Luke/',Luke_view, name="Luke"),
    path('Jamie/',Jamie_view, name="Jamie"),
    path('Manon/',Manon_view, name="Manon"),
    path('Kimbery/',Kimbery_view, name="Kimbery"),
    path('Marisa/',Marisa_view, name="Marisa"),
    path('Lily/',Lily_view, name="Lily"),
    path('Jp/',Jp_view, name="Jp"),
    path('Juri/',Juri_view, name="Juri"),
    path('Dj/',Dj_view, name="Dj"),
    path('Cammy/',Cammy_view, name="Cammy"),
    path('Ryu/',Ryu_view, name="Ryu"),
    path('Honda/',Honda_view, name="Honda"),
    path('Blanka/',Blanka_view, name="Blanka"),
    path('Guile/',Guile_view, name="Guile"),
    path('Ken/',Ken_view, name="Ken"),
    path('Chunli/',Chunli_view, name="Chunli"),
    path('Zangief/',Zangief_view, name="Zangief"),
    path('Dhalsim/',Dhalsim_view, name="Dhalsim"),
    path('Rashid/',Rashid_view, name="Rashid"),
    path('Aki/',Aki_view, name="Aki"),
    path('Ed/',Ed_view, name="Ed"),
    path('Gouki/',Gouki_view, name="Gouki"),
    path('Vega/',Vega_view, name="Vega"),
    path('Terry/',Terry_view, name="Terry"),
    path("<slug>/", post_detail, name="post_detail")
]

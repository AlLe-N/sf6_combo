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

from app.views import frontpage, post_detail,character_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",frontpage,name="frontpage"),
    path('Luke/',character_page, {'character_name': 'luke'}, name="Luke"),
    path('Jamie/',character_page, {'character_name': 'jamie'}, name="Jamie"),
    path('Manon/',character_page, {'character_name': 'manon'}, name="Manon"),
    path('Kimbery/',character_page, {'character_name': 'kimbery'}, name="Kimbery"),
    path('Marisa/',character_page, {'character_name': 'marisa'}, name="Marisa"),
    path('Lily/',character_page, {'character_name': 'lily'}, name="Lily"),
    path('Jp/',character_page, {'character_name': 'jp'}, name="Jp"),
    path('Juri/',character_page, {'character_name': 'juri'}, name="Juri"),
    path('Dj/',character_page, {'character_name': 'dj'}, name="Dj"),
    path('Ryu/',character_page, {'character_name': 'ryu'}, name="Ryu"),
    path('Honda/',character_page, {'character_name': 'honda'}, name="Honda"),
    path('Guile/',character_page, {'character_name': 'guile'}, name="Guile"),
    path('Ken/',character_page, {'character_name': 'ken'}, name="Ken"),
    path('Chunli/',character_page, {'character_name': 'chunli'}, name="Chunli"),
    path('Zangief/',character_page, {'character_name': 'zangief'}, name="Zangief"),
    path('Dhalsim/',character_page, {'character_name': 'dhalsim'}, name="Dhalsim"),
    path('Rashid/',character_page, {'character_name': 'rashied'}, name="Rashid"),
    path('Ed/',character_page, {'character_name': 'ed'}, name="Ed"),
    path('Gouki/',character_page, {'character_name': 'gouki'}, name="Gouki"),
    path('Vega/',character_page, {'character_name': 'vega'}, name="Vega"),
    path('Terry/',character_page, {'character_name': 'terry'}, name="Terry"),
    path('Aki/', character_page, {'character_name': 'aki'}, name='Aki'),
    path('Blanka/', character_page, {'character_name': 'blanka'}, name='Blanka'),
    path('Cammy/', character_page, {'character_name': 'cammy'}, name='Cammy'),
    path("<slug>/", post_detail, name="post_detail")
]

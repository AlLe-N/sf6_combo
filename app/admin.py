from django.contrib import admin

from .models import Post
from .models import Combo

admin.site.register(Post)

admin.site.register(Combo)
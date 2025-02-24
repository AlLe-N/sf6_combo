from django.contrib import admin

from .models import Post
from .models import Combo

admin.site.register(Post)

@admin.register(Combo)
class ComboAdmin(admin.ModelAdmin):
    list_display = ('title', 'character', 'damage')
    list_filter = ('character', 'difficulty')
    search_fields = ('title', 'description')
from django.contrib import admin

from .models import Post
from .models import Character, Combo

admin.site.register(Post)

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Combo)
class ComboAdmin(admin.ModelAdmin):
    list_display = ('title', 'character', 'difficulty', 'damage', 'okizeme')
    list_filter = ('character', 'difficulty', 'okizeme')
    search_fields = ('title', 'description')
from django.contrib import admin

from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Article

@admin.register(Article)
class ArticleAdmin(TranslatableAdmin):
    list_display = ('title', 'created_at')
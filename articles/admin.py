from django.contrib import admin
from articles.models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'pub_date', 'likes')
    list_filter = ['pub_date', 'likes']
    search_fields = ['title']

admin.site.register(Article, ArticleAdmin)

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . models import Articles
from . models import Comments
from . models import ProductsBorsch


class ArticlesAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

admin.site.register(Articles, ArticlesAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'email',
        'article',
        'date',
        'active',
    )
    list_filter = (
        'active',
        'date',
    )
    search_fields = (
        'name',
        'email',
        'text',
    )
admin.site.register(Comments)

admin.site.register(ProductsBorsch)
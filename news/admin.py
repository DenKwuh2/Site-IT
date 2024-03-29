from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_at', 'category', 'updated_at', 'is_published', 'get_photo']
    list_display_links = ['id', 'title']
    search_fields = ["title", "content"]
    list_editable = ['is_published', 'category']
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'view', 'create_at', 'updated_at')
    readonly_fields = ('get_photo', 'view', 'create_at', 'updated_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return 'Фото не установлено'


    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ["title"]


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'

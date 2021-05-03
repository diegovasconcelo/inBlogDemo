from django.contrib import admin
from .models import Page


#custom adminsite view
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'created_at')
    ordering = ('-created_at',)

admin.site.register(Page, PageAdmin)

admin.site.site_header='Proyecto: inBlog'
admin.site.site_title='Panel de administración'
admin.site.index_title='Panel de administración'

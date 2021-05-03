from django.contrib import admin
from .models import Article, Category

#custom adminsite view
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at','updated_at')
    search_fields = ('title', 'content', 'user__username','categories__name')
    list_display = ('title', 'user', 'public','private','created_at')
    list_filter = ('public','user__username','categories__name')
    ordering = ('-created_at',)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category,CategoryAdmin)


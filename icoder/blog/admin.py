from django.contrib import admin
from blog.models import Post, BlogComment

admin.site.register((BlogComment)),
# admin.site.register((Post))
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)
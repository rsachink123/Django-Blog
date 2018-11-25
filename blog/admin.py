
# Register your models here.
from django.contrib import admin
from .models import Post, Comment
#@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created','publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_hierarchy = 'publish'
    ordering = ('status','publish')
admin.site.register(Post,AdminPost)
#@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, AdminComment)

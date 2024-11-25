from django.contrib import admin
from .models import *



class PostsAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'date_in', 'rating')

    list_filter = ('author__user__username', 'date_in', 'rating')








admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Games, PostsAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)


from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'teaching_category')
    list_filter = ('teaching_category',)
    search_fields = ('title', 'description')


admin.site.register(Post, PostAdmin)

from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe
# Register your models here.

# 첫번째 방법
# admin.site.register(Post)

# 두번째 방법
# class PostAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Post,PostAdmin)

@admin.register(Post) # rapping
class PostAdmin(admin.ModelAdmin):
    list_display=['id','photo_tag','message','created_at','updated_at',"message_length","is_public"]
    list_display_links=["message"]
    list_filter=['created_at',"is_public"]
    search_fields=['message']

    def message_length(self,Post):
        return f"{len(Post.message)} 글자"
    
    def photo_tag(self,post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;"/>')
        return None


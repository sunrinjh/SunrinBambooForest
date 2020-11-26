from django.contrib import admin

# Register your models here.
from .models import Post,Comment,Photo
admin.site.register(Comment)
class PhotoInline(admin.TabularInline):
    model = Photo

# Post 클래스는 해당하는 Photo 객체를 리스트로 관리하는 한다. 
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]
admin.site.register(Post,PostAdmin)
admin.site.register(Photo)
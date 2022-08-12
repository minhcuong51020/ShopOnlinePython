from django.contrib import admin
from .models import Author, Publisher, Category, BookItem, BookItemImg, Book
from django.utils.html import mark_safe
# Register your models here.
class BookItemImgModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_Book']
    def image_Book(self, obj):
        return mark_safe(
            '''
                <img src = "/media/{img_url}" style="width: 50px;"/>
            '''.format(img_url=obj.image.name)
        )

class BookModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'publisher', 'category']
    search_fields = ['id', 'title', 'author__name']


admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Book, BookModelAdmin)
admin.site.register(BookItem)
admin.site.register(BookItemImg, BookItemImgModelAdmin)

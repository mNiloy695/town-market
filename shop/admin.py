from django.contrib import admin
from .models import shopModel,ItemModel
from django.utils.html import format_html
# Register your models here.

@admin.register(shopModel)
class ShopModelAdmin(admin.ModelAdmin):
    autocomplete_fields = ['owner'] 
    search_fields=['name','contact_number']


@admin.register(ItemModel)
class ItemModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'shop', 'is_available', 'category', 'preview_image')

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px;"/>', obj.image.url)
        return "-"
    preview_image.short_description = 'Image'

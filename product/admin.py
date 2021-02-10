from django.contrib import admin

# Register your models here.
from product.models import Category, Product, Images


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status', 'image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ['status']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ['category']
    inlines = [ProductImageInline, ]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'image', 'image_tag']
    readonly_fields = ('image_tag', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImagesAdmin)

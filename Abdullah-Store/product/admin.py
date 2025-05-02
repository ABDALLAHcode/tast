from django.contrib import admin
from .models import Product , ProductImages , ProductReview , Brand
from .forms import BrandForm , ProductForm , ProductReviewForm
# Register your models here.

class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]
    form = ProductForm

class BrandAdmin(admin.ModelAdmin):
    form = BrandForm

class ProductReviewAdmin(admin.ModelAdmin):
    form = ProductReviewForm


admin.site.register(Brand, BrandAdmin)
admin.site.register(ProductImages)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
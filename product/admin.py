from django.contrib import admin
from .models import Products, Categories
# Register your models here.
# admin.site.register(Categories)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','quantity', 'cost', 'discount')

    list_editable = ['discount',]
    search_fields = ['name',]
    list_filter = ['discount','quantity', 'category']
    fields = [
        "name",
        "category",
        "slug",
        "image",
        ("cost", "discount"),
        "quantity",
    ]
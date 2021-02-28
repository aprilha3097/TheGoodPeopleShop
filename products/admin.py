from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'charity',
        'price',
        'image'
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)

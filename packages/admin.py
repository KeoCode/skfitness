from django.contrib import admin
from .models import Package, Category

class PackagesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register your models here.
admin.site.register(Package, PackagesAdmin)
admin.site.register(Category, CategoryAdmin)
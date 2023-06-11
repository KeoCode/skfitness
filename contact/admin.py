from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone', 'body')
    list_filter = ('name', 'email')
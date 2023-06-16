from django.contrib import admin

from.models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","stock","price","date_created")

admin.site.register(Product,ProductAdmin)

# Register your models here.

from django.contrib import admin
from orders.models import *
# Register your models here.


class ProductOrderInline(admin.TabularInline):
    model = ProductOrder
    extra = 0



class OrderAdmin(admin.ModelAdmin):
    list_display = [ field.name  for field in Order._meta.fields]
    inlines = [ProductOrderInline]

    class Meta:
        model = Order
admin.site.register(Order, OrderAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = [ field.name  for field in Status._meta.fields]


    class Meta:
        model = Status
admin.site.register(Status, StatusAdmin)

class ProductOrderAdmin(admin.ModelAdmin):
    list_display = [ field.name  for field in ProductOrder._meta.fields]


    class Meta:
        model = ProductOrder

admin.site.register(ProductOrder, ProductOrderAdmin)

class ProductInBasketAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]

    class Meta:
        model = ProductInBasket

admin.site.register(ProductInBasket, ProductInBasketAdmin)

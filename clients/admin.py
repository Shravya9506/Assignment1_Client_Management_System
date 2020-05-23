from django.contrib import admin

from .models import Client, Comment, PurchasedCar


class CommentInline(admin.TabularInline):
    model = Comment

class PurchasedCarInline(admin.TabularInline):
    model = PurchasedCar

class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        PurchasedCarInline,
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Comment)
admin.site.register(PurchasedCar)
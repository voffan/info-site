from django.contrib import admin
from info.models import *

# Register your models here.

admin.site.register(Org)

class NewsAdmin(admin.ModelAdmin):
    list_filter = ['pubDate']
    search_fields = ['title', 'pubDate']

admin.site.register(News, NewsAdmin)
admin.site.register(Release)
admin.site.register(Program)
admin.site.register(CarouselImage)

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['reg_date']

admin.site.register(Order, OrderAdmin)
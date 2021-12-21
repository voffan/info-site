from django.contrib import admin
from info.models import *

# Register your models here.

admin.site.register(Org)
admin.site.register(News)
class AdminNews(admin.ModelAdmin):
    list_filter = ['pubDate']
    search_fields = ['title', 'pubDate']

admin.site.register(Release)
admin.site.register(Program)
admin.site.register(CarouselImage)
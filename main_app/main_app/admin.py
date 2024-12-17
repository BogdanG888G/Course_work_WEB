from django.contrib import admin
from django.utils.html import format_html
from .models import Stand

@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    list_display = ('stand_user', 'stand_name', 'power', 'speed', 'range', 'durability', 'precision', 'potential', 'stand_image_thumbnail', 'user_image_thumbnail')
    list_filter = ('stand_user', 'power', 'speed', 'range', 'durability', 'precision', 'potential')
    search_fields = ('stand_name',)

    def stand_image_thumbnail(self, obj):
        if obj.stand_image:
            return format_html('<img src="{}" width="200" height="200" />'.format(obj.stand_image.url))
        return "-"
    stand_image_thumbnail.short_description = 'Stand Image'

    def user_image_thumbnail(self, obj):
        if obj.user_image:
            return format_html('<img src="{}" width="200" height="200" />'.format(obj.user_image.url))
        return "-"
    user_image_thumbnail.short_description = 'User Image'

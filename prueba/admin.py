from django.contrib import admin
from django.utils.html import format_html
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "preview")
    search_fields = ("titulo",)
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.portada:
            return format_html('<img src="{}" style="height:80px;">', obj.portada.url)
        return "—"
    preview.short_description = "Miniatura"


from django.contrib import admin
from django.utils.html import format_html
from .models import Foto


class FotoAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "preview", "creado")
    search_fields = ("titulo",)
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.imagen:
            # Cloudinary ya te da una URL pública
            return format_html('<img src="{}" style="height:80px;">', obj.imagen.url)
        return "—"
    preview.short_description = "Miniatura"

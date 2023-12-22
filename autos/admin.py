from django.contrib import admin
from .models import Auto
from .models import Fiado
from django.utils.html import format_html
# Register your models here.
class AutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'modelo', 'propietario','problema' , 'whatsapp')
    list_editable = ('problema',)
    search_fields=('titulo', 'telefono', 'propietario',)
    def whatsapp(self, obj):
#fecha = ToString(obj.fecha)
        url = "https://wa.me/+58{0}{1}".format(obj.telefono, "&text=")
        return  format_html("<a style='background: green; padding:5px; border-radius:2px;' href='{}'>Contactar</a>".format(url))
    
    whatsapp.allow_tags = True

class FiadoAdmin(admin.ModelAdmin):
    list_display = ('persona', 'email', 'articulo','monto', 'email')
    search_fields=('persona',)
    
admin.site.register(Auto, AutoAdmin)
        

admin.site.register(Fiado, FiadoAdmin)
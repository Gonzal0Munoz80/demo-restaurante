from django.contrib import admin
from menu.models import categoria, plato 

admin.site.site_header = "Administración de Restaurante"
admin.site.site_title = "BOBUX"
admin.site.index_title = "Panel de Administración"
# Register your models here.


@admin.register(categoria)
class categoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','Orden')
    search_fields = ('nombre',)
    list_filter = ('Orden',)
    ordering = ('Orden',)


@admin.register(plato)
class platoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio_formateado', 'categoria')
    list_filter = ('categoria', 'precio')
    search_fields = ('nombre', 'descripcion')

    @admin.display(description='Precio')
    def precio_formateado(self, obj):
        return f"${obj.precio:.2f}".replace('.', ',')


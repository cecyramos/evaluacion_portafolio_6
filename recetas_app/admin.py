from django.contrib import admin
from .models import Receta

class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'autor', 'fecha_creacion')
    list_filter = ('fecha_creacion', 'autor')
    search_fields = ('nombre',)
    readonly_fields = ('fecha_creacion',)
    
    def save_model(self, request, obj, form, change):
        if not obj.autor:
            obj.autor = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Receta, RecetaAdmin)
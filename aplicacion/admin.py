from django.contrib import admin
from.models import *

class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "mes", "anio")
    list_filter = ("tipo","anio", "mes")
admin.site.register(Curso, CursoAdmin)
admin.site.register(Cuerpo)
admin.site.register(Profesor)
admin.site.register(Cartelera)


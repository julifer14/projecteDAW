from django.contrib import admin
from models import tema, pregunta, puntuacio, preguntaErronea,tipus

# Register your models here.

admin.site.register(tema)
admin.site.register(pregunta)
admin.site.register(puntuacio)
admin.site.register(preguntaErronea)
admin.site.register(tipus)


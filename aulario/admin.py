from django.contrib import admin

# Register your models here.
from .models import Aula, Asignatura, Reserva, User, Curso

admin.site.register(Aula)
admin.site.register(Asignatura)
admin.site.register(Reserva)
admin.site.register(User)
admin.site.register(Curso)
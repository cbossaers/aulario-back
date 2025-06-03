from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    admin = models.BooleanField()

    def __str__(self):
        return self.name, self.email, self.password

class Aula(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name, self.capacity

class Asignatura(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name, self.code

class Curso(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    asignaturas = models.ManyToManyField(Asignatura)

    def __str__(self):
        return self.name, self.capacity

class Reserva(models.Model):
    name = models.CharField(max_length=100)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fecha = models.DateTimeField()


    def __str__(self):
        return self.usuario.name, self.curso.name
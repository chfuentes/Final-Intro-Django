from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string
from django_resized import ResizedImageField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.


class TipoAnuncio(models.Model):
    glosa_tipo = models.CharField(max_length=50)
    ESTADO_CHOICES = [
        ('A', 'Activo'),
        ('I', 'Inactivo')
    ]
    estado = models.CharField(
        max_length=1, choices=ESTADO_CHOICES, default='A')

    def __str__(self) -> str:
        return f"{self.glosa_tipo} ({'Activo' if self.estado == 'A' else 'Inactivo'})"


class Anuncio(models.Model):
    titulo = models.CharField(max_length=75)
    cuerpo = models.TextField()
    slug = models.SlugField(max_length=200, default='none')
    fecha = models.DateTimeField(auto_now_add=True)
    # imagen = models.ImageField(default='sin_imagen.png', blank=True)
    imagen = ResizedImageField(size=[300, 300], quality=75, force_format='PNG')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    tipo = models.ForeignKey(TipoAnuncio, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        while Anuncio.objects.filter(slug=self.slug).exists():
            self.slug += get_random_string(length=4)
        super(Anuncio, self).save(*args, **kwargs)


class LogAnuncio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    fecha = models.DateTimeField(auto_now_add=True)
    accion = models.CharField(max_length=200)

    def __str__(self):
        return f"El usuario {usuario} {accion} con fecha {fecha}"

    @receiver(post_save, sender=Anuncio)
    def crear_log_nuevo_anuncio(sender, instance, created, **kwargs):
        if created:
            LogAnuncio.objects.create(
                usuario=instance.autor, accion="Creacion de Anuncio")
        if not created:
            LogAnuncio.objects.create(
                usuario=instance.autor, accion=f"Edicion de Anuncio {instance.id}")

    @receiver(post_delete, sender=Anuncio)
    def crear_log_eliminar_anuncio(sender, instance, **kwargs):
        LogAnuncio.objects.create(
            usuario=instance.autor, accion="Eliminacion de Anuncio")

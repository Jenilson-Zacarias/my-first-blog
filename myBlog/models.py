from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Postagem(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    text = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_public = models.DateTimeField(blank=True, null=True)

    def publicacao(self):
        self.data_public = timezone.now()
        self.save()

    def __str__(self) -> str:
        return self.titulo

    class Meta:
        verbose_name_plural = 'Minhas Postagens'
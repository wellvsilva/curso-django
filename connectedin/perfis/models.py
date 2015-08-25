#coding: utf-8
# connectedin/perfis/models.py

from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):

        nome = models.CharField(max_length=89, null=False)
        #email = models.CharField(max_length=69, null=False)
        telefone = models.CharField(max_length=15, null=False)
        nome_empresa = models.CharField(max_length=69, null=False)

        contatos =models.ManyToManyField('self')

        usuario =models.OneToOneField(User, related_name="perfil")

        @property
        def email(self):
            return self.usuario.email


        def convidar(self, perfil_convidado):
            Convite(solicitante=self, convidado=perfil_convidado).save()



class Convite(models.Model):

        solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
        convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')


        def aceitar(self):
            self.convidado.contatos.add(self.solicitante)
            self.solicitante.contatos.add(self.convidado)
            self.delete()



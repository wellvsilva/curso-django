#coding: utf-8

from django import forms
from django.contrib.auth.models import User

class RegistrarUsuarioForm(forms.Form):

    nome = forms.CharField(required=True)
    email = forms.CharField(required=True)
    senha = forms.CharField(required=True)
    telefone = forms.CharField(required=True)
    nome_empresa = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False

        user_exists = User.objects.filter(username=self.data['nome']).exists()

        if user_exists:
            self.adiciona_erro('Usuario ja existente')
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors = self._e.setdefault(forms.forms.NON_FIELD_ERROS, forms.utils.ErrorList())
        error.append(message)

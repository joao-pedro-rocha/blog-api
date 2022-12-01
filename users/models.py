from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

from cpf_field.models import CPFField
from phonenumber_field.modelfields import PhoneNumberField

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatório.')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusers precisam ter o campo is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusers precisam ter o campo is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    name = models.CharField(verbose_name='Nome', max_length=100, null=True)
    age = models.IntegerField(verbose_name='Idade', null=True)
    cpf = CPFField(verbose_name='CPF', null=True, blank=True)
    rg = models.CharField(verbose_name='RG', max_length=8, null=True,
                          blank=True)
    phone = PhoneNumberField(verbose_name='Telefone', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

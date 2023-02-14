from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class Usuario (AbstractBaseUser):
  username= models.Charfield ("nombre de usuario", unique=True, max_length=100)
  email=models.EmailField("Correo", max_length=254, unique= True)
  nombres= models.CharField ("nombres", max_length= 200, blank=True, null=True)
  apellidos= models.CharField ("apellidos", max_length= 200, blank= True, null=True)
  imagen = models.ImageField("foto de perfil", upload_to="perfil", height_field=None, max_length=200)
  usuario_activo= models.BooleanField(default= True)


  USERNAME_FIELD= "username"
  REQUIRED_FIELDS = ["email", "apellidos", "nombres"]

  def __str__(self):
    return f'{self.nombres},{self.apellidos}'
  def has_perm(self, perm, obj = None):
    return True

  def has_module_perms(self, app_label):
    return True
  @property
  def is_staff(self):
    return self.usuario_administrador

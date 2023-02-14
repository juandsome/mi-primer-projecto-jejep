from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

#comentario
class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombres, password):

        if not email:
            raise ValueError('El usuario debe tener correo!')
        usuario = self.model(
            username=username,
            email=self.normalize_email(email),
            nombres=nombres,
            password=password,
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
    def create_superuser(self, username, email, nombres, password,**extra_fields):
        usuario= self.create_user(
            email,
            username=username,
            nombres=nombres,
            password=password,


        )

        usuario.save()
        return usuario



class Usuario(AbstractBaseUser):
    username = models.CharField("nombre de usuario", unique=True, max_length=100)
    email = models.EmailField("Correo", max_length=254, unique=True)
    nombres = models.CharField("nombres", max_length=200, blank=True, null=True)
    apellidos = models.CharField("apellidos", max_length=200, blank=True, null=True)
    imagen = models.ImageField("foto de perfil", upload_to="perfil", height_field=None, max_length=200, blank=True,
                               null=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    objects = UsuarioManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "nombres"]

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


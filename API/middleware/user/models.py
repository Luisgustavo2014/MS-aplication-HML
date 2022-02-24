from django.db import models

class Base(models.Model):
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserModel(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name},{ self.cpf}, {self.email}, {self.phone_number}'
from django.db import models

# Create your models here.
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

  class  Meta:
    db_table = 'student'
    managed = True
    verbose_name = 'ModelName'
    verbose_name_plural = 'ModelNames'
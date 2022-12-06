from django.db import models


# Create your models here.
class StudentDetails(models.Model):
    name = models.TextField()
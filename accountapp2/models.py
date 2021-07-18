from django.db import models


# Create your models here.

class HelloColi(models.Model):
    text = models.CharField(max_length=255, null=False)  # 텍스트 최대길이 255, null 값이 있으면 안됨

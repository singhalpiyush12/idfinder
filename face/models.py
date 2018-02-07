

# Create your models here.
from django.db import models

class UploadFile(models.Model):
    image = models.ImageField(upload_to='')

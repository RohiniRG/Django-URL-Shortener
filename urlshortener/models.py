from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=2000)
    uuid = models.CharField(max_length=500)

    def __str__(self):
        return self.uuid

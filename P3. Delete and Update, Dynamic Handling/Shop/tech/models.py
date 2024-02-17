from django.db import models

# Create your models here.

class tiktok(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    Description = models.TextField()
    bootha = models.ImageField(upload_to="boothas")

    def __str__(self):
        return 'TikToker : ' + self.name

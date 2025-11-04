from django.db import models

# Create your models here.


class Services(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services/images/')
    description = models.TextField()
    about = models.TextField()

    def __str__(self):
        return self.title

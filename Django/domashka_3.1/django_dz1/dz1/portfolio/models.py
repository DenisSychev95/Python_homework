from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Info(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/')

    def __str__(self):
        return self.title

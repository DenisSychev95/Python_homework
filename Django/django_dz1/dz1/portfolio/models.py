from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)


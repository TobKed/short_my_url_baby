from django.db import models


class Link(models.Model):
    url         = models.URLField(max_length=2056)
    link_id     = models.CharField(max_length=10, unique=True)

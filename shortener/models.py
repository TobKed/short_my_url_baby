from django.db import models

from . import friendly_id


class Link(models.Model):
    url = models.URLField(max_length=2056)
    link_id = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.url} - {self.link_id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.id and not self.link_id:
            self.link_id = friendly_id.encode(self.id)
            self.save()

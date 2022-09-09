from django.db import models


class Task(models.Model):
    desc = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.desc

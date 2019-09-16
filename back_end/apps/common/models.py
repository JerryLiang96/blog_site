from django.db import models

# navbar的标题表


class Nav(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

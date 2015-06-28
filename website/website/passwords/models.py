from django.db import models


class Passwords(models.Model):
    hashstring = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    dump = models.ForeignKey('Dumps')

class Dumps(models.Model):
    dump = models.CharField(max_length=100)
    hashtype = models.CharField(max_length=30)

    class Meta:
        unique_together = (("dump", "hashtype"),)

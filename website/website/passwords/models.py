from django.db import models


class Passwords(models.Model):
    hashstring = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    dump = models.ForeignKey('Dumps')

class Dumps(models.Model):
    dump = models.CharField(max_length=100)
    hashtype = models.CharField(max_length=30)
    hash_count = models.CharField(max_length=30)
    cracked = models.CharField(max_length=30)
    hash_file = models.CharField(max_length=100)
    password_file = models.CharField(max_length=100)

    class Meta:
        unique_together = (("dump", "hashtype"),)

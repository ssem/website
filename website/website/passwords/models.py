from django.db import models

class Dumps(models.Model):
    name = models.CharField(max_length=100)
    hashtype = models.CharField(max_length=30)
    hash_count = models.CharField(max_length=30)
    cracked = models.CharField(max_length=30)
    hash_file = models.CharField(max_length=100)
    password_file = models.CharField(max_length=100)
    stat_file = models.CharField(max_length=100)

    class Meta:
        unique_together = (("name", "hashtype"),)

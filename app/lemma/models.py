from django.db import models

# Create your models here.
class Lemma(models.Model):
    word = models.CharField(max_length=255)

    def __str__(self):
        return self.word
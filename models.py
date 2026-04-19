from django.db import models

class Alumni(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    graduation_year = models.IntegerField()
    course = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    current_job = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.full_name
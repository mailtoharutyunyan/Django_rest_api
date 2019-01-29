from django.db import models


# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=15)
    user_last_name = models.CharField(max_length=15)
    dob = models.DateTimeField()

    def __str__(self):
        return "%s" % self.user_name

from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=20)
    branch = models.CharField(max_length=100)
    college = models.CharField(max_length=50)
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    



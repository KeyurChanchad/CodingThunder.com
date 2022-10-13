from django.db import models

# Create your models/table here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=20)
    email = models.CharField(max_length=123)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/')
    description = models.TextField()

    def __str__(self):
        return self.name

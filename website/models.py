from django.db import models


# Create your models here.
class SliderHero(models.Model):
    img = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class Projects(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name

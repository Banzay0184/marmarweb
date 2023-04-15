from django.db import models


# Create your models here.
class SliderHero(models.Model):
    img = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class ProjectCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    img = models.ImageField(upload_to='uploads/')
    project = models.ForeignKey('Projects', on_delete=models.CASCADE, related_name="project_image")


class Projects(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, verbose_name='категория')

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)
    work = models.CharField(max_length=255)
    img = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name

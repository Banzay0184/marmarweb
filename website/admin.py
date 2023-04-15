from django.contrib import admin
from .models import *


class ProjectImageAdmin(admin.ModelAdmin):
    pass


class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    max_num = 10
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline, ]


# Register your models here.
admin.site.register(SliderHero),
admin.site.register(Projects, ProjectAdmin),
admin.site.register(ProjectImage, ProjectImageAdmin),
admin.site.register(Team),
admin.site.register(ProjectCategory)

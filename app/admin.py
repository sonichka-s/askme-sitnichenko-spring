from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.User)
admin.site.register(models.Tag)
admin.site.register(models.Question)
admin.site.register(models.Answer)

from django.contrib import admin

from .models import Choice, Question

# register your admins here
admin.site.register(Question)

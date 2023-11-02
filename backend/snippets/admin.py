from django.contrib import admin
from .models import Snippet, Highest

# Register your models here.

admin.site.register(Snippet)
admin.site.register(Highest)

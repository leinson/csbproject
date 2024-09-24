from django.contrib import admin

# Register your models here.
from .models import Question
#username: admin, password: cybersec1
admin.site.register(Question)
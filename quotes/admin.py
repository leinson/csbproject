from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Comment
#username: admin, password: cybersec1
#regular user: tester, cybersec1
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Comment)
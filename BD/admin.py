# coding=utf-8
from django.contrib import admin
from BD import models
# Register your models here.
admin.site.register(models.Faculty)
admin.site.register(models.Students)
admin.site.register(models.Speciality)
admin.site.register(models.Student_subject)
admin.site.register(models.Teachers)
admin.site.register(models.Subjects)
admin.site.register(models.Group)
admin.site.register(models.Kafedra)
admin.site.register(models.Questions)
admin.site.register(models.Tests)
admin.site.register(models.Testirovanie)
admin.site.register(models.Answers)


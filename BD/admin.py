from django.contrib import admin
from BD import models
# Register your models here.
admin.site.register(models.Faculty)
admin.site.register(models.Students)
admin.site.register(models.Speciality)
admin.site.register(models.Student_subject)
admin.site.register(models.Teachers)
admin.site.register(models.Subjects)

def __unicode__(self):
    return self.name_faculty()
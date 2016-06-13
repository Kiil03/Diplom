# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.


class Faculty(models.Model):
    id_facultet = models.AutoField(primary_key=True)
    name_faculty = models.CharField(max_length=50,verbose_name=u"Факультет")

    def __unicode__(self):
        return self.name_faculty

class Speciality(models.Model):
    id_speciality = models.AutoField(primary_key=True)
    faculty = models.ForeignKey(Faculty)
    code = models.CharField(max_length=15)
    name_speciality = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name_speciality

class Kafedra(models.Model):
    id_kafedra = models.AutoField(primary_key=True)
    name_kafedra = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name_kafedra

class Teachers(models.Model):
    id_teacher = models.AutoField(primary_key=True)
    kafedra = models.ForeignKey(Kafedra)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    otchestvo = models.CharField(max_length=50,null=True)
    login = models.CharField(max_length=15)
    password = models.CharField(max_length=15)


class Group(models.Model):
    id_group = models.AutoField(primary_key=True)
    speciality = models.ForeignKey(Speciality)
    group_name = models.CharField(max_length=15)


class Students(models.Model):
    id_student = models.AutoField(primary_key=True)
    group = models.ForeignKey(Group)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    otchestvo = models.CharField(max_length=50, null=True)
    login = models.CharField(max_length=15)
    password = models.CharField(max_length=15)


class Subjects(models.Model):
    id_subject = models.AutoField(primary_key=True)
    kafedra = models.ForeignKey(Kafedra)
    teacher = models.ForeignKey(Teachers)
    speciality = models.ForeignKey(Speciality)
    name_subject = models.CharField(max_length=20)


class Student_subject(models.Model):
    id_rel_st_sub = models.AutoField(primary_key=True)
    student = models.ManyToManyField(Students)
    subject = models.ManyToManyField(Subjects)


class Tests(models.Model):
    id_test = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teachers)
    subject = models.ForeignKey(Subjects)
    date_start = models.DateTimeField
    date_finish = models.DateTimeField
    test_time = models.IntegerField
    count_questions = models.SmallIntegerField

class Answers(models.Model):
    id_answer = models.AutoField(primary_key=True)
    answer = models.CharField(max_length=50)

class Questions(models.Model):
    id_question = models.AutoField(primary_key=True)
    question = models.CharField(max_length= 150)
    answer_code = models.ForeignKey(Answers)


class Testirovanie(models.Model):
    id_testirovania = models.AutoField(primary_key=True)
    test = models.ForeignKey(Tests)
    stud_subj_relation = models.ForeignKey(Student_subject)
    id_quest = models.ForeignKey(Questions)
    stud_answer = models.CharField(max_length=50)
    rating = models.CharField


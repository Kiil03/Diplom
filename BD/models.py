# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser
from django.contrib.auth import base_user
import django.contrib.auth.hashers
# Create your models here.


class Faculty(models.Model):
    id_facultet = models.AutoField(primary_key=True)
    name_faculty = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'

    def __unicode__(self):
        return self.name_faculty

class Speciality(models.Model):
    id_speciality = models.AutoField(primary_key = True)
    faculty = models.ForeignKey(Faculty, verbose_name = 'Факультет')
    code = models.CharField(max_length=15, verbose_name = 'Код')
    name_speciality = models.CharField(max_length=100, verbose_name = 'Название специальности')

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

    def __unicode__(self):
        return u'%s %s' %( self.name_speciality, self.code)

class Kafedra(models.Model):
    id_kafedra = models.AutoField(primary_key=True)
    name_kafedra = models.CharField(max_length=150, verbose_name = 'Название кафедры')

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'

    def __unicode__(self):
        return self.name_kafedra

class Teachers(models.Model):
    id_teacher = models.AutoField(primary_key=True)
    auth = models.OneToOneField(User, default='', verbose_name='Учетная запись')
    kafedra = models.ForeignKey(Kafedra)
    last_name = models.CharField(max_length=50,verbose_name ='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name = 'Имя')
    otchestvo = models.CharField(max_length=50,null=True, verbose_name = 'Отчество')

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __unicode__(self):
        return u'%s %s %s' %( self.last_name, self.first_name, self.otchestvo)


class Group(models.Model):
    id_group = models.AutoField(primary_key=True)
    speciality = models.ForeignKey(Speciality)
    group_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __unicode__(self):
        return  self.group_name



class Students(models.Model):
    id_student = models.AutoField(primary_key=True)
    auth = models.OneToOneField(User, default='', verbose_name='Учетная запись')
    group = models.ForeignKey(Group)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    otchestvo = models.CharField(max_length=50, null=True)
    login = models.CharField(max_length=50)
    pasword = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __unicode__(self):
        return '%s %s %s %s %s'  %(self.group, self.last_name, self.first_name, self.otchestvo, self.auth)

class Subjects(models.Model):
    id_subject = models.AutoField(primary_key=True)
    kafedra = models.ForeignKey(Kafedra, verbose_name= 'Кафедра')
    teacher = models.ForeignKey(Teachers, verbose_name= 'Преподаватель')
    speciality = models.ForeignKey(Speciality, verbose_name= 'Специальность')
    name_subject = models.CharField(max_length=100, verbose_name= 'Название дисциплины')

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

    def __unicode__(self):
        return '%s %s' % ( self.teacher, self.name_subject)


class Student_subject(models.Model):
    id_rel_st_sub = models.AutoField(primary_key=True)
    student = models.ManyToManyField(Students)
    subject = models.ManyToManyField(Subjects)


    class Meta:
        verbose_name = 'Студент-предмет'
        verbose_name_plural = 'Студенты-предметы'

    def __unicode__(self):
        return '%s' %(self.id_rel_st_sub)

class Tests(models.Model):
    id_test = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teachers, verbose_name= 'Преподаватель')
    subject = models.ForeignKey(Subjects, verbose_name= 'Дисциплина')
    date_start = models.DateTimeField(verbose_name='Дата начала тестирования',default='')
    date_finish = models.DateTimeField(verbose_name='Дата окончания тестирования',default='')
    test_time = models.IntegerField(verbose_name='Время тестирования',default='')
    count_questions = models.SmallIntegerField(verbose_name='Количество вопросов',default='')

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __unicode__(self):
        return '%s' % (self.subject)


class Answers(models.Model):
    id_answer = models.AutoField(primary_key=True)
    answer = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __unicode__(self):
        return '%s ' % (self.answer)

class Questions(models.Model):
    id_question = models.AutoField(primary_key=True)
    question = models.CharField(max_length= 150, verbose_name= 'Вопрос')
    answer_code = models.ForeignKey(Answers, verbose_name='Ответ')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __unicode__(self):
        return '%s ' % (self.question)


class Testirovanie(models.Model):
    id_testirovania = models.AutoField(primary_key=True)
    test = models.ForeignKey(Tests, verbose_name='Тестируемая дисциплина')
    stud_subj_relation = models.ForeignKey(Student_subject,verbose_name= 'Студент')
    id_quest = models.ForeignKey(Questions, verbose_name= 'Вопрос')
    stud_answer = models.CharField(max_length=50, verbose_name= 'Ответ')
    rating = models.CharField

    class Meta:
        verbose_name = 'Тестирование'
        verbose_name_plural = 'Тестирования'

    def __unicode__(self):
        return '%s %s %s %s %s' % (self.test, self.stud_subj_relation, self.id_quest, self.stud_answer, self.rating)
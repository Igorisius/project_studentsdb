# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from datetime import datetime
from django.contrib import messages
from PIL import Image

from ..models import Student, Group

# Views for Students
def students_list(request):
    students = Student.objects.all()
# order student_list
    order_by = request.GET.get('order_by', '')
    if request.GET.get('order_by', '') == '':
        request.GET.order_by = 'last_name'
    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()
# paginate students
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        students = paginator.page(paginator.num_pages)

    
    return render(request, 'students/students_list.html',
        {'students': students})

def students_add(request):
# якщо форма була запощена
    if request.method == "POST":
      # якщо кнопка додати натиснута
        if request.POST.get('add_button') is not None:
       # перевіряємо дані на коректність та збираємо помилки
            errors = {}
# data for student object
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}
# validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Ім'я є обов'язковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u"Дата народження є обов'язковою"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    u'Введіть коректний формат дати (напр. 1991-04-10)'
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер квитка є обов'язковим"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Оберіть групу студентів"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Оберіть коректну групу"
                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo', '')
            if not photo:
                errors['photo'] = u"Очевидно, ви ще не завантажили фото студента"
            else:
                    im = Image.open(photo)
                    if im.format not in ('JPEG', 'PNG'):
                        errors['photo'] = u"завантажте фото з розширенням jpeg або png"
                    if photo.size > 3145728:
                        errors['photo'] = u"максимальний розмір фото - 3 мб"
                    else:
                        data['photo'] = photo
       #save student
            if not errors:
                student = Student(**data)
                student.save()
                # status message
                #redirect to student_list
                return HttpResponseRedirect(u'%s?status_message=Студента %s %s успішно додано' % (reverse('home'), first_name, last_name))
            else:
# віддаємо шаблон разом із знайденими помилками
                return render(request, 'students/students_add.html', 
                {'groups': Group.objects.all().order_by('title'),
                'errors': errors})

        elif request.POST.get('cancel_button') is not None:
# redirect to home page on cancel button
            return HttpResponseRedirect(u'%s?status_message=Додавання студента скасовано!' %
reverse('home'))
    else:
# повертаємо код початкового стану форми
        return render(request, 'students/students_add.html',
        {'groups': Group.objects.all().order_by('title')})

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

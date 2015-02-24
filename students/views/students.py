# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students
def students_list(request):
    students = (
        {'id': 1,
        'first_name': u'Іван',
        'last_name': u'Білочка',
        'ticket': 4715,
        'image': 'img/s1.jpg'},
        {'id': 2,
        'first_name': u'Стартапер',
        'last_name': u'Іванович',
        'ticket': 1324,
        'image': 'img/s3.jpg'},
        {'id': 3,
        'first_name': u'Михась',
        'last_name': u'Пилипенко',
        'ticket': 2001,
        'image': 'img/s2.jpg'},
    )

    return render(request, 'students/students_list.html',
        {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
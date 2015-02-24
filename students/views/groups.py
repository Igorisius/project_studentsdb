# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Groups
def groups_list(request):
    groups = (
        {'id': 1,
        'group_number': u'Іп 13',
        'group_leader': u'Сергій Валігура'},
        {'id': 2,
        'group_number': u'Іф 42',
        'group_leader': u'Стефа Зайчиха'},
        {'id': 3,
        'group_number': u'Іпф 23',
        'group_leader': u'Володимир Перший'},
    )   
    return render(request, 'students/groups_list.html',
        {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, sid):
    return HttpResponse('<h1>Edit Group %s</h1>' % sid)

def groups_delete(request, sid):
    return HttpResponse('<h1>Delete Group %s</h1>' % sid)

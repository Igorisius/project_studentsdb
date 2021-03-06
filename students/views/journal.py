# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def journal_list(request):
    journal = (
        {'id': 1,
        'last_name': u'Петро Білочка'},
        {'id': 2,
        'last_name': u'Іван Іванович'},
        {'id': 3,
        'last_name': u'Михайло Пилипенко'},
        {'id': 4,
        'last_name': u'Хтоб Небув'},
    )
    return render(request, 'students/journal_list.html',
        {'journal': journal})

def journal_update(request, sid):
    return HttpResponse('<h1>Update Journal %s</h1>' % sid)


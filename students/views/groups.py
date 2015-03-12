# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import Group
# Views for Groups
def groups_list(request):
    groups = Group.objects.all()

    return render(request, 'students/groups_list.html',
        {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, sid):
    return HttpResponse('<h1>Edit Group %s</h1>' % sid)

def groups_delete(request, sid):
    return HttpResponse('<h1>Delete Group %s</h1>' % sid)

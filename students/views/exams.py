# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import Exam

# Views for Exams
def exams_list(request):
    exams = Exam.objects.all()

# order exams_list
    order_by = request.GET.get('order_by', '')
    if request.GET.get('order_by', '') == '':
        request.GET.order_by = 'exam_name'
    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'exam_name', 'teacher_name', 'exam_day'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()
# paginate exams
    paginator = Paginator(exams, 3)
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        exams = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        exams = paginator.page(paginator.num_pages)


    return render(request, 'students/exams_list.html',
        {'exams': exams})

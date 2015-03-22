from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studentsdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # My Student urls
    url(r'^$', 'students.views.students.students_list', name='home'),
    url(r'^students/add/$', 'students.views.students.students_add',
        name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$',
        'students.views.students.students_edit',
        name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$',
        'students.views.students.students_delete',
        name='students_delete'),


    # My Groups urls
    url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
    url(r'^groups/add/$', 'students.views.groups.groups_add',
        name='groups_add'),
    url(r'^groups/(?P<sid>\d+)/edit/$',
        'students.views.groups.groups_edit',
        name='groups_edit'),
    url(r'^groups/(?P<sid>\d+)/delete/$',
        'students.views.groups.groups_delete',
        name='groups_delete'),

    # My Journal urls
    url(r'^journal/$', 'students.views.journal.journal_list',     name='journal'),
    url(r'^journal/(?P<sid>\d+)/update/$',    'students.views.journal.journal_update',
        name='journal_update'),

  # My Exam urls
    url(r'^exams/$', 'students.views.exams.exams_list', name='exams'),


    url(r'^admin/', include(admin.site.urls)),
)

from .settings import MEDIA_ROOT, DEBUG

if DEBUG:
# serve files from media folder
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT}))



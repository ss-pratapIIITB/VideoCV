from django.conf.urls import patterns, include, url

from django.contrib import admin
from OCVapp.views import home
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OCV.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'OCVapp.views.home', name='home'),
    url(r'^register/$', 'OCVapp.views.register', name='register'), # ADD NEW PATTERN!
    url(r'^login/$', 'OCVapp.views.user_login', name='login'),
    # url(r'^addQuestion/$', 'OCVapp.views.addQuestion', name='addQuestion'),

    # url(r'^addTest/$', 'OCVapp.views.addTest', name='addTest'),

    # url(r'^logout/$', 'OCVapp.views.user_logout', name='logout'),	
    url(r'^giveTest/$', 'OCVapp.views.give_test', name='give_test'),	
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}),
    url(r'^admin/', include(admin.site.urls)),
)

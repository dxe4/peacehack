from django.conf.urls import patterns, include
from theapp import urls as theapp_urls

urlpatterns = patterns(
    '',
    (r'', include(theapp_urls, namespace='theapp', app_name='theapp')),
)

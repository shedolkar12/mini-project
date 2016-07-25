from django.conf.urls import url, include,patterns
from app.views import *

urlpatterns = [
url(r'^dashboard/$', dashboard, name='dashboard'),
url(r'^$', index, name='index'),
]

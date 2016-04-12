"""scratch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from quiz.views import check_answer, do_quiz, select_category

urlpatterns = [
    url(r'^$', select_category, name='select_category'),
    url(r'^(?P<category_id>[0-9]+)/do/$', do_quiz, name='do_quiz'),
    url(r'^check/', check_answer, name='check_answer'),
]

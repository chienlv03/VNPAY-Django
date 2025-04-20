"""vnpay_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.urls import re_path
from django.contrib import admin

import vnpay_python.views

urlpatterns = [
    re_path(r'^$', vnpay_python.views.index, name='index'),
    re_path(r'^index.html$', vnpay_python.views.index, name='index_html'),
    re_path(r'^donate.html$', vnpay_python.views.donate, name='donate'),
    re_path(r'^contact.html$', vnpay_python.views.contact, name='contact'),
    re_path(r'^login.html$', vnpay_python.views.login, name='login'),
    re_path(r'^payment_ipn$', vnpay_python.views.payment_ipn, name='payment_ipn'),
    re_path(r'^payment_return$', vnpay_python.views.payment_return, name='payment_return'),
    re_path(r'^query$', vnpay_python.views.query, name='query'),
    re_path(r'^refund$', vnpay_python.views.refund, name='refund'),
    re_path(r'^admin/', admin.site.urls),
]

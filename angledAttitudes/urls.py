"""angledAttitudes URL Configuration

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
from django.conf.urls import url,patterns
from django.contrib import admin
from django.conf.urls import include
from django.contrib.auth.views import login, logout

from .views import register


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include('django.contrib.auth.urls')),
    # url(r'^login/$', view=login, kwargs={'template_name': 'registration/login.html'}, name="login"),
    # url(r'^logout/$', view=logout, kwargs={'template_name': 'registration/logout.html', 'next_page': '/'}, name="logout"),
    # url(r'^register/$', view=register, name="register"),
    url(r'^', include("chooseASide.urls", namespace="sides")),
]

from . import settings
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
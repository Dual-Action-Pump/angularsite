from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name="all_topics"),
    url(r"^leaderboards/", views.leaderboards, name="leaderboards"),
    url(r"^s/(?P<pk>[\d]+)/", views.increment_score, name="score"),
    url(r"^(?P<topic>[\w\p{P}\'-]+)/your-angle", views.create_angle, name="create_angle"),  # allow user to voice opinion
    url(r"^(?P<topic>[\w\p{P}\'-]+)/", views.topic, name="topic"),  # individual topic
]


from django.conf.urls import (handler404, handler500)

handler404 = 'views.not_found'
handler500 = 'views.error500'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="all_topics"),
    url(r'^(?P<topic>[\w-\']+)/your-angle', views.create_angle, name="create_angle"),  # allow user to voice opinion
    url(r'^(?P<topic>[\w-\']+)/', views.topic, name="topic"),  # individual topic
    # url(r'^(?P<topic>[\w-]+)/all_angles')
]
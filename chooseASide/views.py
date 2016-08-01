import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.db.models import Count

from ipware.ip import get_ip

from . import models
from . import forms

def handler404(request):
    response = render_to_response('chooseASide/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


# Create your views here.
def home(request):
    print(request.META.get("HTTP_USER_AGENT"))  # this
    print("____")
    print(request.META.get("REMOTE_ATTR"))
    all_topics = models.Topic.objects.filter(expired=False).annotate(total_angles=Count('thought', distinct=True))
    if request.method == "POST":
        form = forms.CreateTopicForm(request.POST)
        if form.is_valid():
            new_topic = models.Topic(title=form.cleaned_data['title'],
                                     description=form.cleaned_data['description'])
            new_topic.save()
            return HttpResponseRedirect("/")
    else:
        form = forms.CreateTopicForm()

    return render(request, "chooseASide/topic_list.html", {"topics": all_topics,
                                                               "form": form,})


def topic(request, topic):
    print(topic)
    current_topic = get_object_or_404(models.Topic, title__contains=topic.replace("-", " "))
    pro_views = models.Thought.objects.filter(pro_or_con=True, topic=current_topic).order_by("-score")
    con_views = models.Thought.objects.filter(pro_or_con=False, topic=current_topic).order_by("-score")
    total = float(pro_views.count() + con_views.count())
    print(str(total)+ " total")
    if total == 0:
        pro_percent = 0
        con_percent = 0
    else:
        pro_percent = (pro_views.count()/total)*100
        con_percent = (con_views.count()/total)*100
    return render(request, "chooseASide/topic.html", {'topic': current_topic,
                                                      'pros': pro_views,
                                                      'cons': con_views,
                                                      'pro_percent': pro_percent,
                                                      'con_percent': con_percent})


def create_angle(request, topic):
    topic_in_question = get_object_or_404(models.Topic, title=topic.replace('-', ' '))
    if request.method == "POST":
        form = forms.ThoughtForm(request.POST)
        if form.is_valid():
            ip = get_ip(request)
            if ip is not None:
                iden1 = str(ip)
            else:
                iden1 = ""
            if request.META.get("HTTP_USER_AGENT"):
                iden2 = request.META.get("HTTP_USER_AGENT")
            else:
                iden2 = ""
            if form.cleaned_data['pro_or_con'] == "0":
                pro_or_con = False
                print("should be false")
            else:
                pro_or_con = True
            new_opinion = models.Thought(topic=topic_in_question,
                                         opinion=form.cleaned_data['opinion'],
                                         pro_or_con=pro_or_con,
                                         identifier1=iden1,
                                         identifier2=iden2)
            new_opinion.save()
            return HttpResponseRedirect('/'+topic+'/angles')
    else:
        form = forms.ThoughtForm()
    return render(request, "chooseASide/create_angle.html", {"form": form,
                                                             "topic": topic_in_question})


def increment_score(request,pk):
    if request.method == 'POST':
        to_increment = get_object_or_404(models.Thought,pk=pk)
        print(to_increment.score)
        to_increment.score += 1
        to_increment.save()
        return HttpResponse(json.dumps({"message": "Score incremented",
                                        "current_score": to_increment.score}))
    else:
        return HttpResponse(json.dumps({"message": "Something went wrong"}))


def leaderboards(request):
    # top 5 thoughts by score and topics by number of thoughts
    top_thoughts = models.Thought.objects.all().order_by("-score")[:5]
    top_topics = models.Topic.objects.annotate(total_angles=Count('thought', distinct=True)).order_by("-total_angles")[:5]
    return render(request, "chooseASide/leaderboards.html", {'top_thoughts': top_thoughts,
                                                             'top_topics': top_topics})


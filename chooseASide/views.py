import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Max


from . import models
from . import forms


# Create your views here.
def home(request):
    print(request.META.get("HTTP_USER_AGENT"))  # this
    print("____")
    print(request.META.get("REMOTE_ATTR"))
    all_topics = models.Topic.objects.all()
    if request.method == "POST":
        form = forms.CreateTopic(request.POST)
        if form.is_valid():
            new_topic = models.Topic(title=form.cleaned_data['title'],
                                     description=form.cleaned_data['description'])
            new_topic.save()
            return HttpResponseRedirect("/")
    else:
        form = forms.CreateTopic()

    return render(request, "chooseASide/topic_list.html", {"topics": all_topics,
                                                               "form": form})


def topic(request, topic):
    print(topic)
    current_topic = models.Topic.objects.get(title=topic.replace("-", " "))
    pro_views = models.Topic.objects.filter(pro_or_con=True).aggregate(Max('score'))
    con_views = models.Topic.objects.filter(pro_or_con=False).aggregate(Max('score'))
    print(current_topic.top_con)
    return render(request, "chooseASide/topic.html", {'topic': current_topic, })


def create_angle(request, topic):
    topic_in_question = models.Topic.objects.get(title=topic.replace('-', ' '))
    if request.method == "POST":
        form = forms.ThoughtForm(request.POST)
        if form.is_valid():
            new_opinion = models.Thought(topic=topic_in_question,
                                         opinion=form.cleaned_data['opinion'],
                                         pro_or_con=form.cleaned_data['pro_or_con'])
            new_opinion.save()
            return HttpResponseRedirect('/'+topic+'/angles')
    else:
        form = forms.ThoughtForm()
    return render(request, "chooseASide/create_angle.html", {"form": form,
                                                             "topic": topic_in_question})

def increment_score(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        to_increment = models.Thought.objects.get(pk=pk)
        to_increment.score += 1
        to_increment.save()
        return HttpResponse(json.dumps({"message": "Score incremented",
                                        "current_score": to_increment.score}))
    else:
        return HttpResponse(json.dumps({"message": "Something went wrong"}))

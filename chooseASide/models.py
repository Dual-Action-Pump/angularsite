from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=30, unique=True)
    popularity_score = models.IntegerField(default=0)
    description = models.CharField(max_length=100, default="")
    top_pro = models.ForeignKey("Thought", related_name="top_pro", blank=True, null=True)
    top_con = models.ForeignKey("Thought", related_name="top_con", blank=True,null=True)
    is_company = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(" ", "-")
        super(Topic, self).save(*args, **kwargs)


class Thought(models.Model):
    score = models.IntegerField(default=0)
    topic = models.ForeignKey("Topic")
    opinion = models.TextField(max_length=3000)
    pro_or_con = models.BooleanField(help_text="True is for and on the left, False is against and on the right")
    created = models.DateTimeField(auto_now_add=True)
    identifier1 = models.CharField(help_text="Ip address of the user", max_length=200, default="")
    identifier2 = models.CharField(help_text="Device user is posting from", max_length=30, default="")

    def __str__(self):
        return self.opinion[:30]
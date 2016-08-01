from django.contrib import admin

# Register your models here.
from . import models


class ThoughtAdmin(admin.ModelAdmin):
    list_display = ('opinion', 'topic', 'pro_or_con')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

    def expired(modelAdmin, request, queryset):
        for topic in queryset:
            topic.save()
    actions = [expired]

    def add_view(self, *args, **kwargs):
        self.exclude = ('slug',)
        return super(TopicAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.exclude = ('slug',)
        return super(TopicAdmin, self).change_view(*args, **kwargs)

admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Thought, ThoughtAdmin)
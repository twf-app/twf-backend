from django.contrib import admin

from .models import Tag, JournalEntry, CheckIn, Review

# Register your models here.

admin.site.register(Tag)
admin.site.register(JournalEntry)
admin.site.register(CheckIn)
admin.site.register(Review)

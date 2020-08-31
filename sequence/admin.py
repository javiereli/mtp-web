## Django Packages
from django.contrib import admin
from django.utils.html import format_html
from django.template.response import TemplateResponse
from django.urls import reverse
from django.urls import path
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string

## Custom Libs ##
from lib.functions import send_mail_with_html

## App packages
from .models import *


############################################################################

class TransTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'parent',
        'icon',
        'description'
    )


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description'
    )

class SequenceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'camera_make',
        'seq_key',
        'pano',
        'user_key',
        'username',
        'name',
        'description'
    )

    def get_queryset(self, request):
        query = super(SequenceAdmin, self).get_queryset(request)
        filtered_query = query.filter(is_transport=True)
        return filtered_query

class IconAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'filename'
    )

admin.site.register(TransType, TransTypeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Sequence, SequenceAdmin)
admin.site.register(Icon, IconAdmin)

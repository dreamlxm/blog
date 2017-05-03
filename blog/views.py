# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from blog.models import BlogPost
from django.shortcuts import render_to_response

def archive(request):
    posts = BlogPost.objects.all()
    return render_to_response('archive.html',{'posts':posts})

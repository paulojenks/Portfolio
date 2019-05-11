from django.shortcuts import render
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from django.views.generic import CreateView, DetailView


from datetime import datetime

from . import models
from . import forms


class HomeView(TemplateView):
    template_name = 'my_portfolio/home.html'
    model = models.Project

    def get_context_data(self, **kwargs):
        projects = []
        for project in models.Project.objects.all():
            projects.append(project)
        context = super().get_context_data(**kwargs)
        context['projects'] = projects
        return context


class ProjectNew(CreateView):
    form_class = forms.ProjectForm
    template_name = 'my_portfolio/new_project.html'
    model = models.Project
    success_url = reverse_lazy('my_portfolio:home')


class ProjectView(DetailView):
    model = models.Project

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        projects = []
        for project in models.Project.objects.all():
            projects.append(project)
        context['projects'] = projects
        context['project'] = models.Project.objects.get(pk=pk)
        return context


class AboutView(TemplateView):
    template_name = 'my_portfolio/about.html'


class ContactView(TemplateView):
    template_name = 'my_portfolio/contact.html'



from django import forms

from . import models


class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['name', 'description', 'git_link', 'image', 'type']


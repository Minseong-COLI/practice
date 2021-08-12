from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from projectapp.forms import ProjectCreationForm
from projectapp.models import Project


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    success_url = reverse_lazy('articleapp:list')
    # article list로 임시 지정 -> 이후 detailview 생성후 다시 설정
    template_name = 'projectapp/create.html'


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'


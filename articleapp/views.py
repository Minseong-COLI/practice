from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user
        # login 되어있지 않은 상태에서는 식별되지 않음
        return super().form_valid(form)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp2.decorators import account_ownership_required
from accountapp2.models import HelloColi
from accountapp2.forms import AccountCreationForm
from articleapp.models import Article


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp2/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    # user 객체를 읽어온다
    context_object_name = 'target_user'
    # user를 타겟으로 가져온다
    template_name = 'accountapp2/detail.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        # writer = target_user 와 동일: 작성자 인식
        return super().get_context_data(object_list=article_list, **kwargs)


has_ownership = [login_required(login_url=reverse_lazy('articleapp:login')), account_ownership_required]


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    # success_url = reverse_lazy('accountapp2:detail')
    # 완료 후 이동 페이지
    # pk를 입력해줘야 구동이 됨
    context_object_name = 'target_user'
    template_name = 'accountapp2/update.html'

    def get_success_url(self):
        return reverse('accountapp2:detail', kwargs={'pk': self.object.pk})


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp2/delete.html'

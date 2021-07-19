from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp2.models import HelloColi
from accountapp2.forms import AccountCreationForm


def hello_coli(request):
    # return HttpResponse('Hell Coli')
    # return render(request, 'base.html')
    if request.method == "POST":

        temp = request.POST.get('input_text')

        new_hello_coli = HelloColi()
        new_hello_coli.text = temp
        new_hello_coli.save()
        # 객체를 DB에 저장    # temp와 다르게 DB에 저장됨(왼쪽 파일 목록 db.sqlite3)
        # settings.py의 DATABASE 내용 확인 해보면 지정된걸 확인할수있음

        return HttpResponseRedirect(reverse('accountapp2:hello_coli'))

        # hello_world_list = HelloWorld.objects.all()
        # # DB의 모든 데이터를 hello_world_list에 넣어줌
        #
        # return render(request, 'accountapp/hello_world.html',
        #               context={'hello_world_list': hello_world_list})
    else:
        hello_coli_list = HelloColi.objects.all()
        return render(request, 'accountapp2/hello_coli.html',
                      context={'hello_coli_list': hello_coli_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp2:hello_coli')
    template_name = 'accountapp2/create.html'


class AccountDetailView(DetailView):
    model = User
    # user 객체를 읽어온다
    context_object_name = 'target_user'
    # user를 타겟으로 가져온다
    template_name = 'accountapp2/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    success_url = reverse_lazy('accountapp2:detail')
    # 완료 후 이동 페이지
    # pk를 입력해줘야 구동이 됨
    context_object_name = 'target_user'
    template_name = 'accountapp2/update.html'


class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp2:hello_coli')
    template_name = 'accountapp2/delete.html'

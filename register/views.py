# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from django.views.generic import CreateView
from django.views.generic import FormView
from django.views.generic import DetailView
from django.views.generic import View
from django.views.generic import ListView
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin

from register.models import Record
from register.forms import LoginForm

import csv


class IndexView(CreateView):
    model = Record
    success_url = reverse_lazy('index')
    template_name = 'register/index.html'
    fields = ['name', 'graduate', 'unit', 'phone', 'email', 'im', 'wechat', 'short_word', 'content']


class RecordListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Record
    template_name = 'register/record_list.html'
    paginate_by = 30
    context_object_name = 'record_list'


class RecordDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Record
    template_name = 'register/record_detail.html'
    context_object_name = 'record'


class CreateCSVView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, *args, **kwargs):
        records = Record.objects.all()
        content_disposition = u'attachment; filename=\"已登记人员名单.csv\"'
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = content_disposition.encode('gbk')
        writer = csv.writer(response)
        writer.writerow(map(lambda r: r.encode('gbk'), [
            u'姓名', u'毕业年份', u'现工作单位', u'Email', u'手机', u'QQ', u'微信', u'一句祝语'
        ]))
        rows = map(lambda record: map(lambda r: unicode(r).encode('gbk'),
                                      [record.name, record.graduate, record.unit, record.email, record.phone, record.im,
                                       record.wechat, record.short_word]), records)
        writer.writerows(rows)
        return response


class LogoutView(RedirectView):
    pattern_name = 'index'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class LoginView(FormView):
    template_name = 'register/login.html'
    success_url = reverse_lazy('record_list')
    form_class = LoginForm

    def form_valid(self, form):
        user = form.login()
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return super(LoginView, self).form_valid(form)
            else:
                return self.response_error_page('你的账户尚未激活')
        else:
            return self.response_error_page('用户名或密码错误')

    def response_error_page(self, msg):
        return render(self.request, 'register/info_page.html', {'message': msg})

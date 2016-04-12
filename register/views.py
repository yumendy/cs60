from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView

from register.models import Record


class IndexView(CreateView):
    model = Record
    success_url = reverse_lazy('index')
    template_name = 'register/index.html'
    fields = ['name', 'graduate', 'unit', 'phone', 'email', 'im', 'wechat', 'short_word', 'content']



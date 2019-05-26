from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from notice.models import Notice


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['notice_list'] = Notice.objects.order_by('-created_at')[:4]
        return context


# 계정 등록                                         ch11 2/2
class UserCreateView(CreateView):
  template_name = 'registration/register.html'
  form_class = UserCreationForm
  success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
  template_name = 'registration/register_done.html'


class LoginRequiredMixin(object):
  @classmethod
  def as_view(cls, **initkwargs):
    view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
    return login_required(view
                          )


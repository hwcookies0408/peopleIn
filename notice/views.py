from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic

from userExtends.models import Profile
from .forms import CreatePostForm
from .models import Notice

from django.views.generic import ListView, DetailView, TemplateView

def notice_list(request):
    qs = Notice.objects.all()
    return render(request, 'notice/notice_list.html',
                  {'notice_list': qs})


def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'notice/notice_detail.html',
                  {'notice': notice})




def new_feed(request):
    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드를 실행
        new_article = Notice.objects.create(
            # author=request.author,
            # author=request.POST.get('username'),
             title=request.POST['title'],
            content=request.POST['content'],
        )

        # 새글 등록 끝

    return render(request, 'notice/notice_list.html')

 # paginated_by = 3 # 한 페이지 목록에 표시 게시물 수 (단 한 줄로 페이지네이션이 구현됨)

# def get_context_data(self, **kwargs):
#     context = super(PostListView, self).get_context_data(**kwargs)
#
#     block_size = 5 # 하단의 페이지 목록 수
#
#     start_index = int((context['page_obj'].number - 1) / self.block_size) * self.block_size
#     end_index = min(start_index + self.block_size, len(context['paginator'].page_range))
#
#     context['page_range'] = context['paginator'].page_range[start_index:end_index]
#
#     return context

class PostLV(ListView) :
    model = Notice

class PostDV(DetailView) :
    model = Notice

# *******************************************************************************8888888


























# def post_write(request):
#     if request.method == 'POST':
#         form = CreatePostForm(request.POST)
#
#         if form.is_valid():
#             conn_user = request.user
#             conn_profile = Profile.objects.get(user=conn_user)
#             username = conn_profile.username
#
#             new_post = form.save(commit=False)
#             new_post.author = username
#             new_post.save()
#
#             return render(request,'notice/notice_list.html', {'form' : form})
#         else:
#             form = CreatePostForm()
#
#         return render(request, 'notice/notice_list.html', {'form': form})

# class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
#     model = Notice
#     success_url = reverse_lazy('notice_list')
#
#     def get_queryset(self):
#         conn_user = self.request.author
#         author = get_author(conn_user)
#         return self.model.objects.filter(writer=author)
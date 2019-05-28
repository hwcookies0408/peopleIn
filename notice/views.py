from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render

from .forms import PostForm
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
            author=request.author,
            title=request.POST['title'],
            text=request.POST['content'],
        )

        # 새글 등록 끝

    return render(request, 'notice/new_feed.html')

#  paginated_by = 3 # 한 페이지 목록에 표시 게시물 수 (단 한 줄로 페이지네이션이 구현됨)
#
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

from django.shortcuts import get_object_or_404, render
from .models import Notice


def notice_list(request):
    qs = Notice.objects.all()
    return render(request, 'notice/notice_list.html',
                  {'notice_list': qs})


def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'notice/notice_detail.html',
                  {'notice': notice})



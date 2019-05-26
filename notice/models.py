from django.db import models
from pytz import timezone  # 현지 시각 출력을 위하여
from django.conf import settings
from django.urls import reverse

def local_time(input_time):
    fmt = '%Y-%m-%d %H:%M'
    my_zone = timezone(settings.TIME_ZONE)
    my_local_time = input_time.astimezone(my_zone)
    return my_local_time.strftime(fmt)


class Notice(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # 'auth.User'라고 쓰는 것보다 강추
        on_delete=models.CASCADE,
        related_name='notice',
        verbose_name='게시자',
    )
    title = models.CharField('제목', max_length=100)
    content = models.TextField('내용')
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True)
    hit = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-id']  # notice 객체의 기본 정렬 순서 지정

    def __str__(self):
        return self.title

    def short_content(self):
        if self.content:
            t = self.content[:20] + '...'   # content 속성의 일부만 반환
        else:
            t = '(내용 없음)'
        return t
    short_content.short_description = '간략 내용'

    @property
    def update_counter(self):
        self.hit = self.hit + 1
        self.save()
        return self.hit

    def get_absolute_url(self):
        # return reverse('notice:notice_detail', args=[self.pk])
        return reverse('notice:notice_detail', kwargs={'pk': self.pk}) # reverse 임포트 시켜주어야함.

# blog/admin.py
from django.contrib import admin
from .models import Notice, Comment


@admin.register(Notice)  # 아래 클래스가 Post 모델을 관리하는 클래스임
class NoticeAdmin(admin.ModelAdmin):
    # list_display = ['id', 'author', 'title', 'short_content',   # short content
    #                 ]
    list_display = ['id', 'title', 'short_content',   # short content
]
    # 위에서 'author.username'으로 하면 'not a callable' 오류
    # 위에서 'tags'로 하면 'must not be a ManyToManyField'라고 오류
    list_display_links = ['id', 'title', ]
    list_filter = ['created_at']
    search_fields = ['title', 'content', ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # list_display = ['id', 'post', 'message', 'updated_at', ]  # 바른 현지 시각
    list_display = ['id', 'post', 'message', 'updated', ]
    list_display_links = ['id', 'message', ]

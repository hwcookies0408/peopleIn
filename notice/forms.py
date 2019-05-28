from django import forms  # forms 모델을 import
from .models import Notice  # Post모델 임포트


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ('title', 'content')
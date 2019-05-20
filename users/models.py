from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    userid = models.CharField(max_length=20, unique=True,primary_key=True)
    name = models.CharField(max_length=255, verbose_name='유저 이름')
    birthday = models.CharField(max_length=8, verbose_name='생년월일')
    in_area = models.CharField(max_length=10, verbose_name='관심지역')
    in_job = models.CharField(max_length=10, verbose_name='관심업종')
    phone = models.CharField(max_length=140, verbose_name='전화번호')
    is_admin = models.BooleanField(default=False, verbose_name='관리자 여부')


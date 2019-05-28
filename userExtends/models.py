from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Profile(models.Model):
    GANGNAM = 1
    SUNGDONG = 2
    YEONGDEUNGPO = 3
    GWANGJIN = 4
    MAPO = 5
    SONGPA =6
    AREA_CHOICES = (
        (GANGNAM, '강남구'),
        (SUNGDONG, '성동구'),
        (YEONGDEUNGPO, '영등포구'),
        (GWANGJIN, '광진구'),
        (MAPO, '마포구'),
        (SONGPA, '송파구')
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True, verbose_name='birthdate')
    in_area = models.PositiveSmallIntegerField(choices=AREA_CHOICES, null=True, blank=True, verbose_name='in_area')
    # in_job = models.CharField(max_length=10, verbose_name='관심업종')
    phone = models.CharField(max_length=20, null=True, verbose_name='phone')


    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = (
    (0, '未知'),
    (1, '男'),
    (2, '女'),
    (3, '保密'),
)


class ExtUser(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='关联的用户',
        help_text='关联的用户',
    )
    name = models.CharField(
        max_length=32,
        null=False,
        blank=False,
        verbose_name='姓名',
        help_text='姓名',
    )
    nickname = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name='昵称',
        help_text='昵称',
    )
    gender = models.IntegerField(
        choices=GENDER_CHOICES,
        default=0,
        verbose_name='性别',
        help_text='性别',
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='年龄',
        help_text='年龄',
    )
    mobile = models.CharField(
        max_length=11,
        null=True,
        blank=True,
        verbose_name='手机号',
        help_text='手机号',
    )
    avatar_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        verbose_name='头像',
        help_text='头像',
    )
    wechat_id = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name='微信号',
        help_text='微信号',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '扩展用户'
        verbose_name_plural = '扩展用户'

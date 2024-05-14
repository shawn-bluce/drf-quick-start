# Generated by Django 4.1.13 on 2024-05-14 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='姓名', max_length=32, verbose_name='姓名')),
                ('nickname', models.CharField(blank=True, help_text='昵称', max_length=32, null=True, verbose_name='昵称')),
                ('gender', models.IntegerField(choices=[(0, '未知'), (1, '男'), (2, '女'), (3, '保密')], default=0, help_text='性别', verbose_name='性别')),
                ('age', models.IntegerField(blank=True, help_text='年龄', null=True, verbose_name='年龄')),
                ('mobile', models.CharField(blank=True, help_text='手机号', max_length=11, null=True, verbose_name='手机号')),
                ('avatar_url', models.URLField(blank=True, help_text='头像', max_length=1024, null=True, verbose_name='头像')),
                ('wechat_id', models.CharField(blank=True, help_text='微信号', max_length=32, null=True, verbose_name='微信号')),
                ('user', models.ForeignKey(help_text='关联的用户', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='关联的用户')),
            ],
            options={
                'verbose_name': '扩展用户',
                'verbose_name_plural': '扩展用户',
            },
        ),
    ]

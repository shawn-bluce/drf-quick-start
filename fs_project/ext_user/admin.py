from django.contrib import admin

from ext_user.models import ExtUser


@admin.register(ExtUser)
class ExtUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'nickname', 'gender', 'age', 'mobile', 'avatar_url')
    list_display_links = ('user', 'name')
    list_filter = ('gender', 'age')
    search_fields = ('name', 'nickname', 'mobile')
    list_per_page = 10
    ordering = ('-id',)

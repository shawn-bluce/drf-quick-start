from datetime import date
from rest_framework import serializers
from ext_user.models import ExtUser


class ExtUserSerializer(serializers.HyperlinkedModelSerializer):
    gender_cn = serializers.SerializerMethodField(read_only=True)
    active_cn = serializers.SerializerMethodField(read_only=True)
    joined_days = serializers.SerializerMethodField(read_only=True)

    username = serializers.CharField(source='user.username', read_only=True)
    active = serializers.BooleanField(source='user.is_active', read_only=True)
    date_joined = serializers.DateTimeField(source='user.date_joined', format='%Y-%m-%d %H:%M:%S', read_only=True)

    def get_gender_cn(self, obj):
        return obj.get_gender_display()

    def get_active_cn(self, obj):
        return '正常' if obj.user.is_active else '冻结'

    def get_joined_days(self, obj):
        today = date.today()
        joined_days = (today - obj.user.date_joined.date()).days
        return joined_days

    def validate(self, attrs):
        method = self.context['request'].method
        user = self.context['request'].user

        ext_user_id = self.context['view'].kwargs.get('pk')
        try:
            ext_user = ExtUser.objects.get(id=ext_user_id)
        except ExtUser.DoesNotExist:
            raise serializers.ValidationError(f'用户不存在')

        if method in ('PUT', 'PATCH') and (user.is_superuser or user.id == ext_user.user.id):
            return attrs

        if method in ('DELETE', 'POST') and user.is_superuser:
            return attrs

        raise serializers.ValidationError('您无权进行此操作')

    class Meta:
        model = ExtUser
        fields = [
            'id', 'name', 'username', 'nickname', 'gender',
            'gender_cn', 'avatar_url', 'wechat_id', 'active', 'active_cn',
            'date_joined', 'joined_days',
        ]

from rest_framework import permissions


class IsSuperuserOrReadOnly(permissions.BasePermission):
    """
    自定义权限只允许超级用户进行写操作。
    """

    def has_permission(self, request, view):
        # 任何人都可以进行 GET, HEAD, 或 OPTIONS 请求（即 'list' 和 'detail'）
        if request.method in permissions.SAFE_METHODS:
            return True

        # 只有超级用户可以进行 PUT, PATCH, 和 DELETE 请求
        return request.user and request.user.is_superuser


class IsSuperuserOrCreateOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        elif request.auth and request.user.is_superuser:
            return True

        return False

from rest_framework.permissions import BasePermission, SAFE_METHODS


class SpecialPermission(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated or bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if not request.user.is_staff:
            return obj.user == request.user
        return True
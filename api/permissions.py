from rest_framework import permissions


class IsAdminOrReadOnlyStudent(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser


class IsTheStudent(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        return obj.username == request.user and request.method in permissions.SAFE_METHODS


class BidTheStudent(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        return obj.username == request.user

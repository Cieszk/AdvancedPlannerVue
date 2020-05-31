from rest_framework import permissions


class IsAccountOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

class IsAdminOrDenyAccess(permissions.BasePermission):
        
    def has_permission(self, request, view):
        if request.user.admin:
            return True
        return False

class IsAccountOwnerOrDenyAccess(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

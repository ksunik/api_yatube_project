from rest_framework import permissions

class UpdatePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return super().has_permission(request, view)
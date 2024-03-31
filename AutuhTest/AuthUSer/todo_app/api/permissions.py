from rest_framework import permissions
 

class UserOnlyAccess(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            val = obj.task_user == request.user
            return val
        else:
            val = obj.task_user == request.user
            return val

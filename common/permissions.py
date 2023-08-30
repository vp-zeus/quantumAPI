
from rest_framework.permissions import BasePermission, SAFE_METHODS


class OwnApplicationPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.profile == request.user.profile

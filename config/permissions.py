from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allows read-only access to any user, but only admin users can create, update, or delete.
    """

    def has_permission(self, request, view):
        # Allow all SAFE_METHODS (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # If the request is not a SAFE_METHOD, check if the user is an admin
        return request.user and request.user.is_authenticated and request.user.is_staff

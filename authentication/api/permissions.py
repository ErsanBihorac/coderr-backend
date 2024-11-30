from rest_framework.permissions import BasePermission

class IsAdminForDelete(BasePermission):
    def has_permission(self, request, view):
        """
        Only admins can delete the order.
        """
        if request.method == 'DELETE':
            return request.user and request.user.is_staff
        return True
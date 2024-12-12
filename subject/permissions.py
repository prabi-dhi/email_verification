from rest_framework.permissions import IsAuthenticated

class IsAuthenticatedAdministration(IsAuthenticated):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.user_type == 'ADMINISTRATION':
            return True
        return False
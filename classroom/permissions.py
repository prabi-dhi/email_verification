from rest_framework.permissions import IsAuthenticated

class IsAuthenticatedAdministration(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'ADMINISTRATION'

    
from rest_framework.permissions import IsAuthenticated

class IsAuthenticatedTeacher(IsAuthenticated):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.user_type == 'TEACHER':
            return True
        return False
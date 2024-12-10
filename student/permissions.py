from rest_framework.permissions import IsAuthenticated

class IsAdministrationOrTeacher(IsAuthenticated):  
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.user_type == 'ADMINISTRATION':
            return True
        if request.user.user_type == 'TEACHER':
            return True
        return False

class IsAdministration(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'ADMINISTRATION'
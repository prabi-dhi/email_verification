from rest_framework.permissions import IsAuthenticated

class IsAdministrationOrTeacherSelf(IsAuthenticated):  
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.user_type == 'ADMINISTRATION':
            return True
        if request.user.user_type == 'TEACHER':
            teacher = view.get_object()
            if teacher and teacher.user.id == request.user.id:
                return True
            return False
        return False

class IsAdministration(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'ADMINISTRATION'
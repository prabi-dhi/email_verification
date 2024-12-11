from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.urls import reverse
class CustomPagination(PageNumberPagination):
    page_query_param='p'
    page_size_query_param = 'users'

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })
    def get_next_link(self):
        if not self.page.has_next():
            return None
        return str(self.page.next_page_number())
        # return self._build_page_url(next_page)
    
    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        return str(self.page.previous_page_number())
    
    # def _build_page_url(self, page_number):
    #     url = reverse(self.request.resolver_match.view_name)
    #     return f"{url}?{self.page_query_param}={page_number}"  


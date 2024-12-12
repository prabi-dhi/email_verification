from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_query_param='p'
    page_size_query_param = 'users'

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next page': self.get_next_link(),
            'previous page': self.get_previous_link(),
            'results': data,
        })
    def get_next_link(self):
        if not self.page.has_next():
            return None
        return (self.page.next_page_number())
        # return self._build_page_url(next_page)
    
    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        return (self.page.previous_page_number())
    


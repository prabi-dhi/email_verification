from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

class CustomPagination(LimitOffsetPagination):
    default_limit=2
    limit_query_param='l'
    offset_query_param='o'
    # max_limit=6

    def get_paginated_response(self, data):
        next_page = None
        previous_page = None
        current_page = (self.offset / self.limit)
        if current_page % 1 !=0:
            current_page += 2
            current_page = int(current_page)
        else:
            current_page = int(current_page) + 1            

        if self.get_next_link():
            next_page = current_page + 1

        if self.get_previous_link():
            previous_page = current_page - 1 

        return Response({
            'total_count': self.count,
            'next_page': next_page,
            'current_page':  current_page,  
            'previous_page': previous_page,
            'results': data,

        })

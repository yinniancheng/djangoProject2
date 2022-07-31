from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,render


# class Person(MiddlewareMixin):
#
#     def process_request(self,request):
#         if request.path_info == '/index/':
#             print(111)
#             return
#         else:
#             return HttpResponse("gun")
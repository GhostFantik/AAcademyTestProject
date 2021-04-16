from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


class ResourceView(APIView):
    def get(self, request: Request):
        pass
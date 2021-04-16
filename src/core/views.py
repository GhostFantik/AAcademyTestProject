from django.db.models import F, Sum
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from core.serializations import AllResourcesSerializer, ResourceSerializer
from core.models import Resource


class ResourceView(APIView):
    """View for CRUD operation on resources"""
    def get(self, request: Request):
        resources = Resource.objects.all()
        data = AllResourcesSerializer(resources).data
        return Response(data, status=HTTP_200_OK)

    def post(self, request: Request):
        resource = ResourceSerializer(data=request.data)
        if resource.is_valid():
            resource.save()
            return Response(resource.validated_data, status=HTTP_201_CREATED)
        return Response(resource.errors, status=HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, pk: int):
        return self._update(request, pk, partial=True)

    def put(self, request: Request, pk: int):
        return self._update(request, pk)

    def delete(self, request: Request, pk: int):
        resource = get_object_or_404(Resource, pk=pk)
        resource.delete()
        return Response(ResourceSerializer(resource).data, status=HTTP_200_OK)

    def _update(self, request: Request, pk: int, partial=False):
        resource = get_object_or_404(Resource, pk=pk)
        serializer = ResourceSerializer(resource, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class TotalCost(APIView):
    def get(self, request: Request):
        total_cost = Resource.objects.aggregate(total_cost=Sum(F('price')*F('amount')))
        return Response(total_cost, status=HTTP_200_OK)

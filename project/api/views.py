# Create your views here.
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.renderers import HTMLFormRenderer, JSONRenderer, BrowsableAPIRenderer


from project.api.models import BucketlistsModel, BucketlistItemsModel
from project.api.serializers import BucketlistSerializer, BucketlistItemSerializer


class BucketlistViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    serializer_class = BucketlistSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)

    def list(self, request):
        queryset = BucketlistsModel.objects.all()
        serializer = BucketlistSerializer(
            queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = BucketlistsModel.objects.all()
        bucketlist = get_object_or_404(queryset, pk=pk)
        serializer = BucketlistSerializer(
            bucketlist, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        serializer = BucketlistSerializer(data=request.data,
                                          context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemsViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    serializer_class = BucketlistItemSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)

    def list(self, request):
        queryset = BucketlistItemsModel.objects.all()
        serializer = BucketlistItemSerializer(
            queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = BucketlistItemsModel.objects.all()
        bucketlist = get_object_or_404(queryset, pk=pk)
        serializer = BucketlistItemSerializer(
            bucketlist, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        serializer = BucketlistItemSerializer(data=request.data,
                                              context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import (HTMLFormRenderer,
                                      JSONRenderer, BrowsableAPIRenderer)


from project.api.models import BucketlistsModel, BucketlistItemsModel
from project.api.serializers import (BucketlistSerializer,
                                     BucketlistItemSerializer)


class BucketlistViewSet(viewsets.ViewSet):

    serializer_class = BucketlistSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)

    def list(self, request):
        bucketlist = BucketlistsModel.objects.all()
        serializer = BucketlistSerializer(
            bucketlist, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        bucketlists = BucketlistsModel.objects.all()
        bucketlist = get_object_or_404(bucketlists, pk=pk)
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

    def partial_update(self, request, pk, format=None):
        bucketlist = BucketlistsModel.objects.get(pk=pk)
        serializer = BucketlistSerializer(bucketlist,
                                          context={'request': request},
                                          data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)


class ItemsViewSet(viewsets.ViewSet):

    serializer_class = BucketlistItemSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)

    def list(self, request):
        item = BucketlistItemsModel.objects.all()
        serializer = BucketlistItemSerializer(
            item, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        items = BucketlistItemsModel.objects.all()
        item = get_object_or_404(items, pk=pk)
        serializer = BucketlistItemSerializer(
            item, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        serializer = BucketlistItemSerializer(data=request.data,
                                              context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import (HTMLFormRenderer,
                                      JSONRenderer, BrowsableAPIRenderer)


from project.api.models import Bucketlist, Item
from project.api.serializers import BucketlistSerializer, ItemSerializer


class BucketlistViewSet(viewsets.ViewSet):

    serializer_class = BucketlistSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)

    def list(self, request):
        queryset = Bucketlist.objects.filter()
        serializer = BucketlistSerializer(
            queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Bucketlist.objects.filter()
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

    def partial_update(self, request, pk, format=None):
        queryset = Bucketlist.objects.get(pk=pk)
        serializer = BucketlistSerializer(queryset,
                                          context={'request': request},
                                          data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)


class ItemViewSet(viewsets.ViewSet):

    serializer_class = ItemSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)

    def list(self, request, bucketlist_pk=None):
        queryset = Item.objects.filter(bucketlist_pk=bucketlist_pk)
        serializer = ItemSerializer(
            queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, bucketlist_pk=None):
        queryset = Item.objects.filter(
            bucketlist_pk=bucketlist_pk)
        item = get_object_or_404(queryset, pk=pk)
        serializer = ItemSerializer(
            item, context={'request': request})
        return Response(serializer.data)

    def create(self, request, bucketlist_pk=None):
        serializer = ItemSerializer(data=request.data,
                                    context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

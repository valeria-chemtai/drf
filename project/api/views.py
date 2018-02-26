from rest_framework import viewsets

from project.api.models import Bucketlist, BucketlistItem
from project.api.serializers import BucketlistSerializer, BucketlistItemSerializer


class BucketlistViewSet(viewsets.ModelViewSet):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        serializer.save()


class BucketlistItemViewSet(viewsets.ModelViewSet):
    queryset = BucketlistItem.objects.all()
    serializer_class = BucketlistItemSerializer

    def perform_create(self, serializer):
        serializer.save()

from rest_framework import serializers

from project.api.models import BucketlistsModel, BucketlistItemsModel


class BucketlistSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='bucketlistitemsmodel-detail')

    class Meta:
        model = BucketlistsModel
        fields = ('url', 'pk', 'name', 'intersting',
                  'date_created', 'date_modified', 'items')


class BucketlistItemSerializer(serializers.HyperlinkedModelSerializer):
    bucketlist_pk = serializers.SlugRelatedField(
        queryset=BucketlistsModel.objects.all(), slug_field='pk')

    class Meta:
        model = BucketlistItemsModel
        depth = 4
        fields = ('url', 'pk', 'name',
                  'bucketlist_pk', 'date_created',
                  'date_modified')

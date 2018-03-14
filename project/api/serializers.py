from rest_framework import serializers

from rest_framework_nested.relations import NestedHyperlinkedRelatedField

from project.api.models import Bucketlist, Item


class BucketlistSerializer(serializers.HyperlinkedModelSerializer):
    items = NestedHyperlinkedRelatedField(
        many=True,
        read_only=True,   # Or add a queryset
        view_name='item-detail',
        parent_lookup_kwargs={'bucketlist_pk': 'bucketlist_pk__pk'}
    )
    # items = serializers.HyperlinkedIdentityField(
    #     view_name='bucketlistitemsmodel-detail', many=True,
    #     lookup_url_kwarg='bucketlist_pk'
    # )

    class Meta:
        model = Bucketlist
        fields = ('url', 'pk', 'name', 'interesting',
                  'date_created', 'date_modified', 'items')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    bucketlist_pk = serializers.SlugRelatedField(
        queryset=Bucketlist.objects.all(), slug_field='pk')

    class Meta:
        model = Item
        depth = 4
        fields = ('url', 'pk', 'name',
                  'bucketlist_pk', 'date_created',
                  'date_modified')

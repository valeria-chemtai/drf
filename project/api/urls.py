# from rest_framework import routers
from rest_framework_nested import routers

from django.conf.urls import include, url

from project.api.views import BucketlistViewSet, ItemViewSet


bucketlist_list = BucketlistViewSet.as_view({'get': 'list',
                                             'post': 'create'})
bucketlist_detail = BucketlistViewSet.as_view({'get': 'retrieve'})
item_list = ItemViewSet.as_view({'get': 'list',
                                 'post': 'create'})
item_detail = ItemViewSet.as_view({'get': 'retrieve'})

router = routers.DefaultRouter()

router.register(r'bucketlists', BucketlistViewSet,
                base_name='bucketlist')
router.register(r'items', ItemViewSet, base_name='bucketlistitemsmodel')


bucketlist_router = routers.NestedSimpleRouter(router, r'bucketlists',
                                               lookup='bucketlist')
bucketlist_router.register(r'items', ItemViewSet,
                           base_name='item')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(bucketlist_router.urls))
]

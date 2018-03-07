from rest_framework import routers

from project.api.views import BucketlistViewSet, ItemsViewSet


bucketlist_list = BucketlistViewSet.as_view({'get': 'list',
                                             'post': 'create'})
bucketlist_detail = BucketlistViewSet.as_view({'get': 'retrieve',
                                               'post': 'create'})
item_list = ItemsViewSet.as_view({'get': 'list',
                                  'post': 'create'})
item_detail = ItemsViewSet.as_view({'get': 'retrieve',
                                    'post': 'create'})

router = routers.DefaultRouter()

router.register(r'bucketlists', BucketlistViewSet,
                base_name='bucketlistsmodel')
router.register(r'items', ItemsViewSet, base_name='bucketlistitemsmodel')

urlpatterns = router.urls

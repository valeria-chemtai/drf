from rest_framework import routers

from project.api.views import BucketlistViewSet, BucketlistItemViewSet

router = routers.DefaultRouter()

router.register(r'bucketlists', BucketlistViewSet)
router.register(r'items', BucketlistItemViewSet)

urlpatterns = router.urls

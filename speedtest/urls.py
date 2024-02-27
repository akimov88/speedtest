from rest_framework.routers import SimpleRouter

from speedtest.views import SpeedTestViewSet


router = SimpleRouter(trailing_slash=False)
router.register(prefix='results', viewset=SpeedTestViewSet)
urlpatterns = router.urls

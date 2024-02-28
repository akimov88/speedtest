from django.urls import path
from rest_framework.routers import SimpleRouter

from speedtest.views import SpeedTestViewSet, SpeedTestResultView


router = SimpleRouter(trailing_slash=False)
router.register(prefix='results_list', viewset=SpeedTestViewSet)
urlpatterns = router.urls
urlpatterns.append(path('result', SpeedTestResultView.as_view()))

from rest_framework import routers

from Contact import views

router = routers.DefaultRouter()
router.register(r'', views.ContactViewSet, basename='contact')

urlpatterns = router.urls
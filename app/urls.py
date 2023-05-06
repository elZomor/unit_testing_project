from rest_framework.routers import DefaultRouter

from app.views import StudentViewSet

router = DefaultRouter()

router.register(
    "students", StudentViewSet, basename="student-viewset"
)

urlpatterns = router.urls

from django.urls import path, include
from rest_framework.routers import SimpleRouter

from study.views import MyLessonsViewSet, MylessonsByProductViewSet


router = SimpleRouter()
router.register('my-lessons', MyLessonsViewSet, 'my-lessons')


urlpatterns = [
    path('by-product/<int:product_id>/lessons/', MylessonsByProductViewSet.as_view({'get':'list'})),
    path('', include(router.urls))
]
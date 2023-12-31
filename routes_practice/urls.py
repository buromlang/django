from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookView
from rest_framework import routers

# router = routers.SimpleRouter()
router = DefaultRouter()

router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('test/', BookView.as_view())
]

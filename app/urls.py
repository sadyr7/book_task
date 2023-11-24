from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/books/<int:pk>/get_book_by_id/', BookViewSet.as_view({'get': 'get_book_by_id'}), name='get_book_by_id'),

]

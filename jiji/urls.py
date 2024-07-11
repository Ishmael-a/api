from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, RegionViewSet, ProductViewSet, CartViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

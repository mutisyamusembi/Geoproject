from rest_framework.routers import SimpleRouter
from .views import ProductViewset, CategoryViewset, OrderViewset, OrderItemViewset

router = SimpleRouter()
router.register("products", ProductViewset, basename="products")
router.register("category", CategoryViewset, basename="category")
router.register("order", OrderViewset, basename="order")
router.register("orderitem", OrderItemViewset, basename="orderitems")

urlpatterns = router.urls

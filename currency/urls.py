from .views import CurrencyModelViewSet, PurchasedCurrenciesModelViewSet
from rest_framework.routers import DefaultRouter

app_name = "currency"
router = DefaultRouter()

# currency
router.register("currency", CurrencyModelViewSet, basename="currency")
router.register("purchased_currencies", PurchasedCurrenciesModelViewSet, basename="purchased_currencies")

urlpatterns = []
urlpatterns += router.urls
from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token




urlpatterns=[

    path("category/",include("api.category.urls")),
    path("product/",include("api.product.urls")),
    path("accounts/",include("api.accounts.urls")),
    path("order/",include("api.order.urls")),
    path("payment/",include("api.payment.urls")),
    path("api_auth_token/",obtain_auth_token,name="api_auth_token"),

]
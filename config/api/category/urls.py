from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.SimpleRouter()
router.register("",views.CategoryViewSet,basename="category_list")



urlpatterns=[

    path("",include(router.urls)),
    
]
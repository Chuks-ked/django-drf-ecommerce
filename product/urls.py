from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router =  DefaultRouter()
router.register(r'category', views.CategoryViewSet)

 
urlpatterns = [
    path('api/', include(router.urls))
]

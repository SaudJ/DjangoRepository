from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from firstapp.views import UserViewSet, ArticleViewSet


router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('article', ArticleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/', include('firstapp.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))

]

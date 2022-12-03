from django.contrib import admin
from django.urls import path, include

from . import views

from rest_framework import routers, serializers, viewsets
from .views import UserViewSet
from django.conf.urls.static import static
from django.conf import settings
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('cart', views.cart_info, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('order', views.order, name='order'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

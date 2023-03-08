
from django.urls import path, re_path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings
from django.views.generic import TemplateView
routes = getattr(settings, 'REACT_ROUTES', [])
urlpatterns = [
    # path('<str:model>/', views.HomeListView.as_view(), name='home'),
    re_path(r'^.*$', TemplateView.as_view(template_name='base/index.html')),
    path('api/', views.get_routes,name='home-api'),
    path('api/products/', views.get_products, name='get-products'),
    path('api/product/<str:pk>', views.get_product, name='get-product'),
    path('user/profile/', views.get_user_profile, name='get_user_profile'),
    path('users/', views.get_users, name='get_users'),
    path('users/register/', views.register_user, name='register_user'),

    # API token urls
    # path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]



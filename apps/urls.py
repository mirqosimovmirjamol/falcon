from django.contrib import admin
from django.urls import path
from root import settings
from django.conf.urls.static import static
from apps.views import(
    ProductListView, ProductDetailView,
    ProfileView, SettingsView,
    UserRegisterView, UserLoginView,UserLogoutView
)

urlpatterns = [
    
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    
    
    path('profile/', ProfileView.as_view(), name='profile'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('create/', UserRegisterView.as_view(), name='create_user'),
    path('login/', UserLoginView.as_view(), name='login_user'),
    path('logout/', UserLogoutView.as_view(), name='logout_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

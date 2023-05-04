from django.contrib import admin
from django.urls import path, include
from freelancers.views import register
from freelancers import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('', include('freelancers.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
]

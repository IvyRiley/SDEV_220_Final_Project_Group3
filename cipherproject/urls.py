from django.contrib import admin
from django.urls import path
from cipherapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('cipher/', views.cipher_view, name='cipher'),
    path('history/', views.history_view, name='history'),
    path('about/', views.about, name='about'),
]
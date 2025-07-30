from django.contrib import admin
from django.urls import path
from cipherapp import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Django admin interface
    path('admin/', admin.site.urls),

    # User authentication routes
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    # Main cipher (encrypt/decrypt) page
    path('cipher/', views.cipher_view, name='cipher'),

    # User's message history page
    path('history/', views.history_view, name='history'),

    # About page
    path('about/', views.about, name='about'),
]
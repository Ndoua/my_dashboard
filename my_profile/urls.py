from django.urls import path
from . import views
from .views import contact, contact_success

urlpatterns = [
    path('', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('email/', contact, name='email'),
    path('success/', views.profile, name='success'),
]

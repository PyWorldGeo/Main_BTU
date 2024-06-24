from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('profile/', views.profile, name='profile'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('reading/<str:id>/', views.reading, name='reading'),
    path('adding/<str:id>/', views.adding, name='adding'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_page, name='register')
]
from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    # path('', views.home_page, name='home_page'),
    path('', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('activate/<uidb64>/<token>/', views.user_verify, name="activate"),    
]

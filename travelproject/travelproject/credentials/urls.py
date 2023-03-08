from django.urls import path

from credentials import views
from travelproject import settings
from django.conf.urls.static import static

urlpatterns = [

    path('register', views.register, name='register'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
]
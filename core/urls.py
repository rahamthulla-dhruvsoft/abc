from django.urls import path
from core import views

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('', views.SignUpView.as_view(), name='signUp'),
    path('', views.Helloview.as_view(), name='hello'),
    path('', views.AccesToken.as_view(), name='AccessToken'),
]
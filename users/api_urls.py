from django.urls import path, include
from .views import RegisterView, LoginView

app_name = 'users'

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('sign_in', LoginView.as_view(), name='sign_in'),
]
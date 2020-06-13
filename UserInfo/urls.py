from django.conf.urls import url
from . import views

urlpatterns = [
    url('create_user/', views.UserCreate.as_view(), name='create-user'),
]
from django.urls import path
from . import views

urlpatterns = [
    path("auth/login/", views.login),
    path("auth/signup/", views.signup),
    path("roles/", views.role_list),
    path('roles/<int:role_id>', views.role_detail)
]

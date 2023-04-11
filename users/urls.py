from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginPage, name = "login"),
    path("logout/", views.logoutPage, name = "logout"),
    path("register/", views.UserRegistration, name = "register"),
    
    path("", views.profiles, name = 'profiles'),
    path("user_profile/<str:pk>/", views.user_profile, name = "user_profile"),
    path("account/", views.userAccount, name = "account"), 
    path("edit_account/", views.edit_account, name = "edit_account"),

    path("create_skill/", views.create_skill, name = "create_skill"),
    path("update_skill/<str:pk>", views.update_skill, name = "update_skill"),
    path("delete_skill/<str:pk>", views.delete_skill, name = "delete_skill"),
] 
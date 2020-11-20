from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('', TemplateView.as_view(template_name='index.html')), 
    path('', views.home, name='home'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    # path('account/', views.accountSettings, name="account"),

    path('products/', views.products, name="products"),

    path('products/personal_care/', views.PersonalCare, name="personalcare"),

    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name="check/password_reset.html"),
    name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="check/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="check/password_reset_form.html"), 
    name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="check/password_reset_done.html"), 
        name="password_reset_complete"),

]


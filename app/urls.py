from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.loginpage, name="loginpage"),
    path('loginpage', views.loginpage, name='loginpage'),
    path('signuppage', views.signuppage, name='signuppage'),
    path('feedbackpage', views.feedbackpage, name='feedbackpage'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('verify_email', views.verify_email, name='verify_email'),
    path('setpasswordpage', views.setpasswordpage, name='setpasswordpage'),
    path('forgotpasswordpage', views.forgotpasswordpage, name='forgotpasswordpage'),
    path('setpassword', views.setpassword, name='setpassword'),
    path('homepage', views.homepage, name='homepage'),
    path('profilepage', views.profilepage, name='profilepage'),
    path('logout', views.logout, name='logout'),
    path('update_profile', views.update_profile, name='update_profile')
]

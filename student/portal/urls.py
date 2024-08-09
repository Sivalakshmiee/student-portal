from django.urls import include, path
from portal import views

urlpatterns = [
    path('',views.home, name = "home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin, name="handlelogin")
]

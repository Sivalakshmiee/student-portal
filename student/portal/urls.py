from django.urls import include, path
from portal import views

urlpatterns = [
    path('',views.home, name = "home")
]

from django.urls import path
from .views import my_logout,DashboardView,home
from django.views.generic.base import  TemplateView

urlpatterns = [
    path('',home,name="home"),

    path('logout/',my_logout),

    path("dashboard", DashboardView.as_view(), name='dashboard')

]

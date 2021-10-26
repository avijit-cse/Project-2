from django.urls import path
from  code_main import views



urlpatterns = [
    path('',views.index,name="home"),
    path('like/<pk>/',views.likes,name="like"),
    path('unlike/<pk>/',views.unlikes,name="unlike"),
]





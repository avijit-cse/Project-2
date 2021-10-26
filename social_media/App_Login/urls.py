from django.urls import path
from App_Login import views

urlpatterns = [
    path('singup/',views.singup,name="sing_up"),
    path('login/',views.login_page,name="login"),
    path('edit/',views.edit_profile,name="edit"),
    path('logout/',views.log_out,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('user/<username>/',views.user,name="user"),
    path('follow/<username>/',views.follow,name="follow"),
    path('unfollow/<username>/',views.unfollow,name="unfollow"),

]

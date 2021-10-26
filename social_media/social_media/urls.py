from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from code_main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/',include('code_main.urls')),
    path('account/',include('App_Login.urls')),
    path('',views.index,name="home"),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from django.contrib.auth import views as authentication_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),
    # User Login
    path('register/', user_views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    # Profile
    path('profile/',user_views.profilePage, name = 'profile')
]

urlpatterns += [
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

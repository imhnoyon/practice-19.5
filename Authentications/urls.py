from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('signin/',views.Register,name='signin'),
    path('login/',views.users_login.as_view(),name='login'),
    path('profile/',views.Profile,name='profile'),
    path('logout/',views.Logoutviews,name='logouts'),
    
    path('passChanges/',views.UserPass_change,name='passChanges'),
]
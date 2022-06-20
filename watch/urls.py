from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('register',views.Register, name='register'),
    path('login/',views.Login, name='login'), 
    path('logout/',views.Logout, name='logout'),
    path('profile/',views.UserProfile, name='profile'),
    path('update/',views.ProfileUpdate, name='update'),
    path('home/',views.Home, name='home'),
    path('post/',views.CreatePost, name='post'),
    path('create/',views.CreateHood, name='create'),
    path('hood/',views.Hood, name='hood'),
    path('hoodupdate/',views.HoodUpdate, name='hoodupdate'),
    path('business/',views.CreateBusiness, name='business'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
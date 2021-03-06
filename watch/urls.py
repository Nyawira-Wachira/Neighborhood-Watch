from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.Index, name='index'),
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
    path('businesslist/',views.NewBusiness, name='businesslist'),
    path('bizupdate/',views.BizUpdate, name='bizupdate'),
    path('hospital/',views.Hospital, name='hospital'),
    path('security/',views.Security, name='security'),
    path('search/', views.search_results, name='search_results'),
    path('searchhood/', views.search_hoods, name='search_hoods'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
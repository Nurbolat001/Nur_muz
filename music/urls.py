from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('muz_all/', views.muz_all, name='muz_all'),
    path('add_muz/', views.add_muz, name='add_muz'),
    path('list_genres/', views.list_genres, name='list_genres'),
    path('update_music/<int:song_id>/', views.update_music, name='update_music'),
    path('delete_music/<int:song_id>/', views.delete_music, name='delete_music'),
    path('view_music/<int:genre_id>/', views.view_music, name='view_music'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path("user/register/", views.register_view, name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

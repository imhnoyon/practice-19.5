from django.urls import path
from . import views
urlpatterns = [
    
    path('createAlbum',views.AlbumCreateView.as_view(),name='CrateAlbum'),
    path('editAlbum/<int:id>',views.EditAlbum.as_view(),name='editAlbum'),
    path('deleteAlbum/<int:id>',views.DeleteAlbum.as_view(),name='deleteAlbum'),
    
]


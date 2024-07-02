from django.urls import path
from . import views
urlpatterns = [
    path('',views.listview.as_view(),name='listview'),
    path('musician/',views.MusicianCreateview.as_view(),name='musician'),
    path('edit/musician/<int:id>',views.MusicianUpdateView.as_view(),name='edit_musician'),
    path('delete/musician/',views.MusicianDeleteView.as_view(),name='delete_musician'),
    
    
]

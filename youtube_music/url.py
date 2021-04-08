from django.urls import path,re_path
from . import views

urlpatterns =[
path('',views.index,name='index'),
path('music/',views.music,name='music'),
path('music_now/',views.music_now,name='music_now')
# path('play_pause/<slug:player_id>',views.play_music,name='play_pause')

]

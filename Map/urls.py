from Map.views import render_main, render_cover, render_profile, render_about, render_map, render_security, update_user_groups
from django.urls import path


urlpatterns = [
    path('', render_cover, name='cover'),
    path('main/', render_main, name='main'),
    path('main/profile', render_profile, name='profile'),
    path('main/profile/security', render_security, name='security'),
    path('main/about', render_about, name='about'),
    path('main/map', render_map, name='map'),
    path('main/user_groups', update_user_groups, name='uug'),
]


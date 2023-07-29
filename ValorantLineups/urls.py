from django.urls import path

from ValorantLineups import views

urlpatterns = [
    # path('', views.agents_list, name='home'),
    path('', views.AgentsList.as_view(), name='agents'),
    path('home', views.AbilityList.as_view(), name='home'),
    path('video/', views.VideoList.as_view(), name='video'),
    path('contact/', views.Contact.as_view(), name='contact'),
    # path('register/', views.UserCreateView.as_view(), name='register'),
    path('favorite_videos/', views.FavoriteVideosView.as_view(), name='favorite'),
    # path('maps/', views.MapList.as_view(), name='maps'),

]


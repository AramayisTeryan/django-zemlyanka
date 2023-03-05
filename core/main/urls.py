from django.urls import path
from .import views

urlpatterns=[
    path('', views.HomeListView.as_view(), name='index'),
    path('about/',views.StoryListView.as_view(), name='about'),
    path('menu/', views.MenuListView.as_view(), name = 'menu'),
    path('news/', views.UpdateListView.as_view(), name = 'news'),
    path('contact/', views.ContactListView.as_view(), name = 'contact'),
    path('news-detail/', views.DetailListView.as_view(), name = 'news-detail')   
]
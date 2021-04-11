from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:pk>/like/', views.like, name='like'),
    path('hashtags/<int:hashtag_pk>/', views.hashtag, name='hashtag'),
    # path('<int:pk>/comments/<int:comment_pk>/delete/')
]

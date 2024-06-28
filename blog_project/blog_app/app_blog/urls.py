from django.urls import path
from . import views

urlpatterns = [
    
    path('create_post/', views.create_post, name='create_post'),
    path('post_list/', views.post_list, name='post_list'),
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
    path('<int:post_id>/delete_post/', views.delete_post, name='delete_post'),
    path('edit_post/', views.edit_post_list, name='edit_post_list'),
    path('delete_post_list/', views.delete_post_list, name='delete_post_list'),
    path('filter_postby_author/', views.filter_postby_author, name='filter_postby_author'),
    path('filter_postby_tag/', views.filter_postby_tag, name='filter_postby_tag'),
    
]
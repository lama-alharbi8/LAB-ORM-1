from django.urls import path
from . import views

app_name= 'posts'

urlpatterns=[
    path('create/', views.create_post_view, name= 'create_post_view'),
    path('detail/<post_id>/', views.post_detail_view, name='post_detail_view'),
    path('update/<post_id>/', views.post_update_view, name= "post_update_view"),
    path('delet/<post_id>/', views.post_delete_view, name= "post_delete_view"),
    path('all/posts/', views.all_posts_view,name="all_posts_view"),
    path('search/', views.search_post_view, name='search_post_view'),
]
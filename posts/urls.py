from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path('create/', views.create_galery, name="create_galery"),
    path('new/', views.new_galery, name = "new_galery"),
    path('<int:id>/', views.show_galery, name="show_galery"),
    path('update/<int:id>/', views.update_galery, name="update_galery"),
    path('delete_galery/<int:id>/', views.delete_galery, name="delete_galery"),
    
    path('<int:id>/create_post/', views.create, name="create"),
    path('<int:id>/new_post/', views.new, name = "new"),
    path('<int:id>_post/', views.show, name="show"),
    path('<int:id>/update_post/', views.update, name="update"),
    path('<int:id>/delete_post/', views.delete, name="delete"),
    path('<int:id>/like_post/', views.like, name="like"),
    
    path('<int:id>/create_comment/', views.create_comment, name="create_comment"),
    path('<int:id>/new_comment/', views.new_comment, name="new_comment"),
    path('<int:id>/delete_comment/', views.delete_comment, name="delete_comment"),
    path('<int:id>/update_comment/', views.update_comment, name="update_comment"),
    path('<int:id>/like_comment/', views.like_comment, name="like_comment"),
]
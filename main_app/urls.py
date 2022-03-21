from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('cats/', views.CatList.as_view(), name="cat-list"),
    path('about/', views.About.as_view(), name="about"),
    path('cats/new/', views.CatCreate.as_view(), name="cat_create"),
    path('cats/<int:pk>/', views.CatDetail.as_view(), name="cat_detail"),
    path('cats/<int:pk>/update', views.CatUpdate.as_view(), name="cat_update"),
    path('cats/<int:pk>delete', views.CatDelete.as_view(), name="cat_delete")
]
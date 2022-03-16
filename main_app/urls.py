from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('cats/', views.CatList.as_view(), name="cat-list"),
    #important note: the "/" comes AFTER the url param you want
    path('about/', views.About.as_view(), name="about")
]
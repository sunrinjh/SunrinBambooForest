from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('write/<int:post_id>', views.write, name='write'),
    path('write/',views.postWrite,name='postWrite')
]
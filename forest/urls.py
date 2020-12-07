from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('remove/<int:post_id>', views.remove, name='remove'),
    path('remove_comment/<int:comment_id>', views.remove_comment, name='remove_comment'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('write/<int:post_id>', views.write, name='write'),
    path('write/',views.postWrite,name='postWrite'),
    path('current/',views.current,name='current'),
    path('best/',views.best,name='best'),
    path('good/<int:post_id>',views.good,name='good'),
    path('cancleLike/<int:post_id>',views.cancleLike,name='cancleLike'),
    path('search/',views.search,name='search'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
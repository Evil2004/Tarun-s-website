# importing views.py from posts app
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
   path('post/<int:post_id>', views.post, name='post'),
]

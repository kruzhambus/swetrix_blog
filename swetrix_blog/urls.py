from django.contrib import admin
from django.urls import path

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('<int:pk>/', views.detail, name='detail'),
    path('profile/', views.profile, name='users-profile'),
    path('<str:name>/', views.category, name='category'),
    path('post/<int:pk>/', views.get_post, name='specific_post'),
    path('add_post/', views.add_post, name='add_post'),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()

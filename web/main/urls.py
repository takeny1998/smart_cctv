from django.contrib import admin
from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.index),
    path('events/', views.event_list, name='events'),
    path('events/<int:event_id>', views.event_play, name='play'),
    path('streaming/', views.streaming, name='streaming'),
]
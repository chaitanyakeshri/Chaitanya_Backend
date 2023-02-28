from django.urls import path
from django.contrib import admin
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/', views.getEvent, name='get-event'),
    path('add/', views.addEvent, name='add-items'),
    path('update/<str:pk>/', views.updateEvent, name='update-event'),
    path('delete/<str:pk>/', views.deleteEvent, name='delete-event'),
]

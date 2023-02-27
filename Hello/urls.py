
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "IIT BOMBAY EVENTS MANAGER PORTAL"
admin.site.site_title = "ADMIN "
admin.site.index_title = "EVENTS MANAGER PORTAL"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('api.urls'))
]

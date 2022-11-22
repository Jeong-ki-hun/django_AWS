from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ob/', include('ob.urls')),
    path('admin/', admin.site.urls),
]
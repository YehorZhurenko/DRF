from django.contrib import admin
from django.urls import path
from servusers.views import ServusersAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/servuserslist/', ServusersAPIView.as_view()),
    path('api/v1/servuserslist/<int:pk>/', ServusersAPIView.as_view()),
    
]

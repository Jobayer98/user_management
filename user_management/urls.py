from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def index(request):
    urls = {
        "sing-up": "http://127.0.0.1:8000/api/auth/sign-up",
        "users": "http://127.0.0.1:8000/api/users",
    }
    return Response(urls)

urlpatterns = [
    path('', index, name="home route"),
    path('api/', include('user_api.urls')),
    path('api/auth/', include('auth_api.urls')),
    path('admin/', admin.site.urls),
]

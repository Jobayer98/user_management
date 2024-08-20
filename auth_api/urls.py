from django.urls import path
from .views import RegistrationView

urlpatterns = [
    path('sign-up', RegistrationView.as_view(), name='token_obtain_pair'),
]
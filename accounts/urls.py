from django.urls import path
from .views import SingUpView

urlpatterns = [
    path("sign_up/", SingUpView.as_view(), name="sign_up"),
]
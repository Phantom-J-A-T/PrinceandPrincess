from django.urls import path
from .views import SignupView, user_detail

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('user-detail/', user_detail, name='user-detail'),
]

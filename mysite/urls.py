from django.contrib import admin
from django.urls import path

# from kek.views import receive_request
from kek.views import MyTokenObtainPairView, MyTokenRefreshView, MyTokenVerifyView, register_user

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('signup', receive_request, name='receive_request'),
    path('signup', register_user, name='receive_user_data'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', MyTokenVerifyView.as_view(), name='token_verify'),
    path('api/register/', register_user, name='register_user'),
]
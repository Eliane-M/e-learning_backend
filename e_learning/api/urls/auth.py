from django.urls import path
from api.views.authentication.login import login_api
from api.views.authentication.register import new_user
from api.views.authentication.token import CustomTokenObtainPairView


urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', new_user, name='register'),
    path('login/', login_api, name='login'),
]
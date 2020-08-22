from django.contrib import admin
from django.urls import path
from application import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drug/', views.DrugView.as_view()),
    path('drug/<int:pk>', views.DrugView.as_view()),
    path('vaccination/', views.VaccinationRudView.as_view()),
    path('vaccination/<int:pk>', views.VaccinationRudView.as_view()),
    path('token/', views.TokenView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

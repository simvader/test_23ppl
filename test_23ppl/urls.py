from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    path('drugs/', views.DrugView.as_view()),
    path('drug/', views.DrugView.as_view()),
    path('drugs/<int:pk>', views.DrugRudView.as_view()),
    path('drug/<int:pk>', views.DrugRudView.as_view()),
    path('vaccination/', views.VaccinationView.as_view()),
    path('vaccination/<int:pk>', views.VaccinationRudView.as_view()),
    path('token/', views.TokenView.as_view()),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

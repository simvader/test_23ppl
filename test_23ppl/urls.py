from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drug/', views.DrugView.as_view()),
    path('drug/<int:pk>', views.DrugView.as_view()),
    path('vaccination/', views.VaccinationRudView.as_view())
    path('vaccination/<int:pk>', views.VaccinationRudView.as_view())
    path('token/', views.TokenView.as_view())
]

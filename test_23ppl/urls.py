from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drug/', views.DrugView.as_view()),
    path('vaccination/', views.VaccinationView.as_view())
]

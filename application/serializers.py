from rest_framework import serializers
from .models import (
    Drug,
    Vaccination
)


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'


class VaccinationSerializer(serializers.ModelSerializer):
    drug_id = serializers.IntegerField(
        write_only=True
    )
    
    class Meta:
        model = Vaccination
        fields = '__all__'

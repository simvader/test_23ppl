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
    drug = DrugSerializer(
        read_only=True
    )

    class Meta:
        model = Vaccination
        fields = '__all__'

    def validate_rut(self, value):
        """Custom validation for rut"""
        rut = value.upper()
        rut = rut.replace(".", "")
        aux = rut[:-1]
        dv = rut[-1:]
        reversed = map(int, reversed(str(aux)))
        factors = cycle(range(2,8))
        a = sum(d * f for d, f in zip(reversed, factors))
        res = (-a)%11
        if str(res) == dv:
            return aux
        else:
            raise serializers.ValidationError("Rut is not valid.")

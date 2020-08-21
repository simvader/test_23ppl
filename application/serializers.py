from rest_framework import serializers
from .models import (
    Drug,
    Vaccination
)
from itertools import cycle


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
        run = value.upper()
        run = run.replace('-', '')
        run = run.replace('.', '')
        try:
            validated = int(run)
        except ValueError:
            raise serializers.ValidationError("Rut is not valid.")
        aux = run[:-1]
        dv = run[-1:]
        reversed_digits = map(int, reversed(str(aux)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        if str((-s) % 11) == dv:
            return run
        elif dv=='K' and ((-s) % 11) == 10:
            return run
        else:
            raise serializers.ValidationError("Rut is not valid.")

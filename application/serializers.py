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


class DrugUpdateSerializer(serializers.ModelSerializer):
    """Allow update only a few attributes"""
    name = serializers.CharField(required=False)
    code = serializers.CharField(required=False)
    description = serializers.CharField(required=False)

    class Meta:
        model = Drug
        fields = ('name', 'code', 'description')


class VaccinationUpdateSerializer(serializers.ModelSerializer):
    """Allow update only a few attributes"""
    rut = serializers.IntegerField(
        write_only=True, required=False
    )
    drug = DrugSerializer(
        read_only=True
    )
    drug_id = serializers.IntegerField(required=False)
    dose = serializers.FloatField(required=False)
    date = serializers.DateTimeField(required=False)

    class Meta:
        model = Vaccination
        fields = '__all__'

    def validate_drug_id(self, value):
        try:
            drug = Drug.objects.get(pk=value)
            return value
        except Drug.DoesNotExist:
            raise serializers.ValidationError("Drug does not exists.")

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

    def validate_dose(self, value):
        if value  < 0.15 or value > 1.0:
            raise serializers.ValidationError(
                "Ensure dose its between 0.15 and 1.0 cm3 inclusive"
            )
        else:
            return value


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

    def validate_drug_id(self, value):
        try:
            drug = Drug.objects.get(pk=value)
            return value
        except Drug.DoesNotExist:
            raise serializers.ValidationError("Drug does not exists.")

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

    def validate_dose(self, value):
        if value  < 0.15 or value > 1.0:
            raise serializers.ValidationError(
                "Ensure dose its between 0.15 and 1.0 cm3 inclusive"
            )
        else:
            return value

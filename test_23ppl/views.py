from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import (
    DrugSerializer,
    VaccinationSerializer
)


class DrugView(APIView):

    def get(self, request):
        """Get all Drugs."""
        serializer = DrugSerializer(
            Drug.objects.all(),
            many=True
        )
        return Response(serializer.data)


class VaccinationView(APIView):

    def get(self, request):
        """Get all vaccinations."""
        serializer = VaccinationSerializer(
            Vaccination.objects.all(),
            many=True
        )
        return Response(serializer.data)

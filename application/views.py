from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Drug,
    Vaccination,
)
from django.contrib.auth.models import User
from django.http import Http404
from .serializers import (
    DrugSerializer,
    VaccinationSerializer
)
from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


class DrugView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """Get all Drugs."""
        serializer = DrugSerializer(
            Drug.objects.all(),
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = DrugSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class DrugRudView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            Drug.objects.get(pk=pk)
        except Drug.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        drug = self.get_object(pk)
        serializer = DrugSerializer(drug)
        return Response(serializer.data)

    def put(self, request, pk):
        drug = self.get_object(pk)
        serializer = DrugSerializer(drug, data=request.data)
        if serialiser.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        drug = self.get_object(pk)
        drug.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VaccinationView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        """Get all vaccinations."""
        serializer = VaccinationSerializer(
            Vaccination.objects.all(),
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = VaccinationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class VaccinationRudView(APIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            Vaccination.objects.get(pk=pk)
        except Vaccination.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        vaccination = self.get_object(pk)
        serializer = VaccinationSerializer(vaccination)
        return Response(serializer.data)

    def put(self, request, pk):
        vaccination = self.get_object(pk)
        serializer = VaccinationSerializer(vaccination, data=request.data)
        if serialiser.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        vaccination = self.get_object(pk)
        vaccination.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TokenView(APIView):

    def get(self, request):
        user = User.objects.get(pk=1)
        t = Token.objects.filter(user_id=1)
        t.delete()
        token = Token.objects.create(user=user)
        return Response({
            'token': token.key
        })

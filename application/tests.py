from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from application.models import Drug
from rest_framework.authtoken.models import Token

class VaccinationTestCase(APITestCase):

    def test_vaccination_without_auth(self):
        """Testing unauthorized request"""
        data = {"rut": "17.861.821-0", "dose": 0.6, "date": "2000-01-01 00:00", "drug_id": 1}
        response =  self.client.post("/vaccination/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class VaccinationAuthorizedTestCase(APITestCase):

    def api_authentication(self):
        self.user = User.objects.create_user(username="dummy_user", password="dummy_psswd")
        self.token = Token.objects.create(user=self.user)

    def populate_drug(self):
       drug = Drug()
       drug.name = "Aspirina"
       drug.code = "A001"
       drug.description = "Para el dolor de cabeza"
       drug.save()

    def test_vaccination_with_auth(self):
        """Authorize dummy user for next test"""
        self.api_authentication()
        self.populate_drug()
        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)
        response = self.client.post("/vaccination/", {"rut": "17.861.821-0", "dose": 0.6, "date": "2000-01-01 00:00", "drug_id": 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class VaccinationWrongRutTestCase(APITestCase):

     def api_authentication(self):
        self.user = User.objects.create_user(username="dummy_user", password="dummy_psswd")
        self.token = Token.objects.create(user=self.user)


     def populate_drug(self):
       drug = Drug()
       drug.name = "Aspirina"
       drug.code = "A001"
       drug.description = "Para el dolor de cabeza"
       drug.save()

     def test_vaccination_wrong_rut(self):
        """Authorize dummy user for next test"""
        self.api_authentication()
        self.populate_drug()
        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)
        response = self.client.post("/vaccination/", {"rut": "17.816d1.821-0", "dose": 0.6, "date": "2000-01-01 00:00", "drug_id": 1})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

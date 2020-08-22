from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status


class VaccinationTestCase(APITestCase):

    def test_vaccination(self):
        data = {"rut": "17.861.821-0", "dose": 0.6, "date": "2000-01-01 00:00", "drug_id": 1}
        response =  self.client.post("/vaccination/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

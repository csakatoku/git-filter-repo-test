from rest_framework import status
from rest_framework.test import APITestCase


class VersionTestCase(APITestCase):
    def test_get_version(self):
        response = self.client.get("/api/version")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.json(), {"version": "1.0.0"})

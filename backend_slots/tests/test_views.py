from backend_slots.factories import SlotFactory
from django.test import TestCase
from rest_framework.test import APIClient


class SlotListTestCase(TestCase):
    def test_slot_list_empty(self):
        client = APIClient()
        response = client.get("/api/slots/test")

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.json(), [])

    def test_slot_list_filled(self):
        for count, h in enumerate(range(15, 18)):
            SlotFactory.create(
                item_id="test",
                date=f"2022-07-31T{h:02d}:00:00Z",
                count=count,
            )

        client = APIClient()
        response = client.get("/api/slots/test")

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(
            response.json(),
            [
                {
                    "id": 1,
                    "date": "2022-07-31T15:00:00Z",
                    "count": 0,
                    "item_id": "test",
                },
                {
                    "id": 2,
                    "date": "2022-07-31T16:00:00Z",
                    "count": 1,
                    "item_id": "test",
                },
                {
                    "id": 3,
                    "date": "2022-07-31T17:00:00Z",
                    "count": 2,
                    "item_id": "test",
                },
            ],
        )

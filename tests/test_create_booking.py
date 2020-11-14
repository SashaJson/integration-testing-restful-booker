from random import randint

from api import random


class TestCreateBooking:

    def test_create_new_booking(self, client):
        data = random.random_booking()
        res = client.create_booking(data)
        assert res.status_code == 200
        created = res.json()
        assert created.get("bookingid")
        assert created.get("booking") == data

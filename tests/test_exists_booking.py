from random import randint

from api import random


class TestExistsBooking:

    def test_new_booking_exists(self, client):
        data = random.random_booking()
        res = client.create_booking(data)
        created = res.json()
        bookingid = created.get("bookingid")
        res = client.get_booking(bookingid)
        exists = res.json()
        assert exists == data

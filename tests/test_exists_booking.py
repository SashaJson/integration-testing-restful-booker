from random import randint

from api import random


class TestExistsBooking:

    def test_new_booking_exists(self, client):
        data = random.random_booking()
        res = client.create_booking(data)
        assert res.status_code == 200
        created = res.json()
        bookingid = created.get("bookingid")
        res = client.get_booking(bookingid)
        assert res.status_code == 200
        exists = res.json()
        assert exists == data

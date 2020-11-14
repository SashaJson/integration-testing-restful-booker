from random import randint

from api import random


class TestExample:

    def test_update_booking(self, client):
        data = random.random_booking()
        res = client.create_booking(data)
        created = res.json()
        bookingid = created.get("bookingid")
        data2 = random.random_booking()
        res = client.update_booking(bookingid, data2)
        updated = res.json()
        assert updated == data2


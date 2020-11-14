from random import randint

from api import random


class TestUpdateBooking:

    def test_update_booking(self, client):
        data = random.random_booking()
        res = client.create_booking(data)
        assert res.status_code == 200
        created = res.json()
        bookingid = created.get('bookingid')
        data2 = random.random_booking()
        res = client.update_booking(bookingid, data2)
        assert res.status_code == 200
        updated = res.json()
        assert updated == data2
        res = client.delete_booking(bookingid)
        assert res.status_code == 201


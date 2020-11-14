from random import randint

from api import random


class TestUpdateBookingPartial:

    def test_update_booking_partial(self, client):
        data = random.random_booking()
        res = client.create_booking(data)
        assert res.status_code == 200
        created = res.json()
        bookingid = created.get('bookingid')
        data2 = random.random_booking_partial()
        res = client.partial_update_booking(bookingid, data2)
        assert res.status_code == 200
        updated = res.json()
        assert updated.get('firstname') == data2.get('firstname')
        assert updated.get('lastname') == data2.get('lastname')
        res = client.delete_booking(bookingid)
        assert res.status_code == 201

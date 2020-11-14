from random import randint

from api import random


class TestExistsBooking:

    def test_new_booking_exists(self, client):
        data = random.random_booking()
        res = client.create_booking(data)
        assert res.status_code == 200
        created = res.json()
        bookingid = created.get('bookingid')
        res = client.get_all_booking()
        assert res.status_code == 200
        exists = res.json()
        for x in exists:
            if x['bookingid'] == bookingid:
                break
        else:
            assert False
        res = client.delete_booking(bookingid)
        assert res.status_code == 201

    def test_new_booking_exists_by_id(self, client):
        data = random.random_booking()
        res = client.create_booking(data)
        assert res.status_code == 200
        created = res.json()
        bookingid = created.get('bookingid')
        res = client.get_booking_by_id(bookingid)
        assert res.status_code == 200
        exists = res.json()
        assert exists == data
        res = client.delete_booking(bookingid)
        assert res.status_code == 201
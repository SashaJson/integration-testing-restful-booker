from api import random


class TestExample:

    def test_create_new_booking(self, client):
        data = random.random_booking()
        res = client.vr(client.create_booking(data))
        created = res.json()
        assert created.get("bookingid")
        assert created.get("booking") == data

    def test_new_booking_exists(self, client):
        data = random.random_booking()
        res = client.vr(client.create_booking(data), [200, 201])
        created = res.json()
        bookingid = created.get("bookingid")
        res = client.vr(client.get_booking(bookingid))
        exists = res.json()
        assert exists == data

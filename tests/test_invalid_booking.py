from random import randint

from api import random


class TestInvalidBooking:

    def test_not_existing_booking(self, client):
        res = client.get_booking(randint(10000, 99999))
        assert res.status_code == 404

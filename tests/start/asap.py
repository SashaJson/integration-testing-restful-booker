from tests.test_example import TestExample
from conftest import client

c = client()

TestExample.test_create_new_booking(c)
from unittest import TestCase
from hamcrest import *
from pyseed.hello import hello


class TestHello(TestCase):
    def test_hello(self):
        assert_that(hello("roger"),  equal_to("hello roger"))

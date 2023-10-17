import pytest


@pytest.yield_fixture()
def setup():
    print("This method called before every methods")
    yield
    print("run after method")


def testM1(setup):
    print("simple pytest code from m1")


def testM2(setup):
    print("message from m2")

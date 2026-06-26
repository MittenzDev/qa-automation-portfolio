import pytest
import time


@pytest.fixture(autouse=True)
def slow_down():
    yield
    time.sleep(1)

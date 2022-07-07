import pytest

@pytest.fixture(scope="function",name="desired_caps")
def case_init():
    print("module1 before")
    yield
    print("module1 end")
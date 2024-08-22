import pytest


@pytest.fixture
def prices():
    return [100, 200, 300]


#@pytest.mark.parametrize("tax_rate, expected", [(10, [110, 220, 330]),
                                                #(15, [115, 230, 345]),
                                               # (20, [120, 240, 360]),])

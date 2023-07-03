import DoubleDiamond
from DoubleDiamond import Balance, spinwheel

def test_default_initial_balance():
    test_balance = Balance(47)
    assert test_balance.total == 47
    assert spinwheel() in {"-","=","≡","7","%","◇"}

import DoubleDiamond
from DoubleDiamond import Balance, spinwheel, play_or_quit
from io import StringIO


def test_default_initial_balance(monkeypatch):
    mock_input = StringIO("yes\n")
    monkeypatch.setattr('sys.stdin', mock_input)
    monkeypatch.setattr("DoubleDiamond.play_or_quit", lambda x: "yes")
    test_balance = Balance(47)
    assert test_balance.total == 47
    assert spinwheel() in {"-","=","≡","7","%","◇"}

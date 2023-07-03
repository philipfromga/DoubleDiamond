from DoubleDiamond import spinwheel
monkeypatch.setattr('run_app', io.StringIO('yes'))
def test1():
    assert spinwheel() in {"-","=","≡","7","%","◇"}

from script import do_something


class TestScript():

    def test_do_something(self):
        result = do_something()
        assert result == 1

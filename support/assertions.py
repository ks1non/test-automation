from support.custom_errors import AssertionsErrors


class Assertions:
    @staticmethod
    def assert_equal(actual, expected):
        assert actual == expected, AssertionsErrors.ERROR_EQUAL.format(expected, actual)

    @staticmethod
    def assert_text(actual, expected):
        assert actual == expected, AssertionsErrors.ERROR_TEXT.format(expected, actual)

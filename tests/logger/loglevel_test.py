import pytest

from src.logger.errors import UnknownLogLevelError
from src.logger.loglevel import LogLevel


class TestLogLevel:
    """Test suite for LogLevel enum."""

    def test_from_str_valid(self) -> None:
        """Test conversion of string representations to LogLevel enum values.

        This test verifies that:
            - Uppercase strings match their corresponding enum values
            - Case-insensitive matching works (lowercase strings also match)
            - All defined log levels can be converted
        """
        assert LogLevel.from_str("DEBUG") == LogLevel.DEBUG
        assert LogLevel.from_str("debug") == LogLevel.DEBUG
        assert LogLevel.from_str("INFO") == LogLevel.INFO
        assert LogLevel.from_str("WARNING") == LogLevel.WARNING
        assert LogLevel.from_str("ERROR") == LogLevel.ERROR
        assert LogLevel.from_str("CRITICAL") == LogLevel.CRITICAL

    def test_from_str_invalid(self) -> None:
        """Test error handling for invalid string conversions.

        This test verifies that:
            - Non-existent log level names raise ValueError
            - The error message contains "Invalid log level" to help with debugging
            - The validation prevents incorrect string values from being accepted
        """
        with pytest.raises(UnknownLogLevelError, match="Invalid log level"):
            LogLevel.from_str("INVALID")

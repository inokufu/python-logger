import pytest

from src.logger.loglevel import LogLevel


class TestLogLevel:
    """Test suite for LogLevel enum."""

    def test_from_str_valid(self) -> None:
        """Test that valid strings are converted to LogLevel."""
        assert LogLevel.from_str("DEBUG") == LogLevel.DEBUG
        assert LogLevel.from_str("debug") == LogLevel.DEBUG
        assert LogLevel.from_str("INFO") == LogLevel.INFO
        assert LogLevel.from_str("WARNING") == LogLevel.WARNING
        assert LogLevel.from_str("ERROR") == LogLevel.ERROR
        assert LogLevel.from_str("CRITICAL") == LogLevel.CRITICAL

    def test_from_str_invalid(self) -> None:
        """Test that invalid strings raise ValueError."""
        with pytest.raises(ValueError, match="Invalid log level"):
            LogLevel.from_str("INVALID")

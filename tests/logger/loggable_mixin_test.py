from unittest.mock import Mock

import pytest

from src.logger.loggable_mixin import LoggableMixin


class TestLoggableMixin:
    """Test suite for LoggableMixin."""

    @pytest.fixture
    def loggable(self) -> LoggableMixin:
        """Create a LoggableMixin instance for testing.

        Returns:
            LoggableMixin: A fresh instance of the mixin for testing.
        """
        return LoggableMixin()

    def test_logger_not_set(self, loggable: LoggableMixin) -> None:
        """Test error handling when accessing logger before setting it.

        This test verifies that:
            - Accessing the logger property before setting it raises a RuntimeError
            - The error message correctly indicates "Logger not set"

        Args:
            loggable: Fresh LoggableMixin instance without a logger set
        """
        with pytest.raises(RuntimeError, match="Logger not set"):
            _ = loggable.logger

    def test_logger_set(self, loggable: LoggableMixin, mock_logger: Mock) -> None:
        """Test logger property setter and getter functionality.

        This test verifies that:
            - The logger can be successfully assigned through the property setter
            - The same logger instance is retrieved through the property getter
            - No exceptions are raised when accessing properly set logger

        Args:
            loggable: Fresh LoggableMixin instance
            mock_logger: Mock object simulating a logger implementation
        """
        loggable.logger = mock_logger
        assert loggable.logger == mock_logger

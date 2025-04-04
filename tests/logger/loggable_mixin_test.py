from unittest.mock import Mock

import pytest

from src.logger.loggable_mixin import LoggableMixin


class TestLoggableMixin:
    """Test suite for LoggableMixin."""

    @pytest.fixture
    def loggable(self) -> LoggableMixin:
        """Create a LoggableMixin instance."""
        return LoggableMixin()

    def test_logger_not_set(self, loggable: LoggableMixin) -> None:
        """Test that accessing logger before setting raises RuntimeError."""
        with pytest.raises(RuntimeError, match="Logger not set"):
            _ = loggable.logger

    def test_logger_set(self, loggable: LoggableMixin, mock_logger: Mock) -> None:
        """Test setting and getting logger."""
        loggable.logger = mock_logger
        assert loggable.logger == mock_logger

import io
from collections.abc import Mapping
from typing import Any

import pytest
from loguru import logger

from src.logger.loglevel import LogLevel
from src.logger.loguru import LoguruLogger


class TestLoguruLogger:
    """Test suite for Loguru logger."""

    @pytest.fixture
    def loguru_logger(self) -> LoguruLogger:
        """Create a LoguruLogger instance for testing.

        Returns:
             Configured LoguruLogger instance
        """
        return LoguruLogger(level=LogLevel.DEBUG)

    @pytest.fixture
    def capture_logs(self) -> io.StringIO:
        """Capture logs output to a string buffer.

        Yields:
            StringIO buffer containing log output
        """
        log_stream = io.StringIO()
        logger.remove()
        logger.add(log_stream, format="{message}")
        yield log_stream
        logger.remove()

    @pytest.mark.parametrize(
        ("level", "message", "context"),
        [
            ("debug", "Debug message", {"key": "value"}),
            ("info", "Info message", None),
            ("warning", "Warning message", {"key": "value"}),
            ("error", "Error message", {"error": "value"}),
            ("critical", "Critical message", None),
        ],
    )
    def test_log_levels(
        self,
        loguru_logger: LoguruLogger,
        capture_logs: io.StringIO,
        level: str,
        message: str,
        context: Mapping[str, Any] | None,
    ) -> None:
        """Test all logging levels with various message/context combinations.

        Args:
            loguru_logger: Logger instance
            capture_logs: String buffer capturing log output
            level: Log level to test
            message: Message to log
            context: Optional context dictionary
        """
        # Get logging method dynamically
        log_method = getattr(loguru_logger, level)

        # Log with or without context
        log_method(message, context=context)

        # Get logged output
        logs = capture_logs.getvalue()

        # Verify message is present
        assert message in logs

        # Verify context if provided
        if context:
            for key, value in context.items():
                assert f"'{key}': '{value}'" in logs

    def test_exception_log(
        self,
        loguru_logger: LoguruLogger,
        capture_logs: io.StringIO,
    ) -> None:
        """Test exception logging with context.

        The test verifies that:
            - Exception message is properly logged
            - Exception type is included
            - Additional context is preserved
        """
        try:
            raise ValueError("Sample exception")  # noqa: TRY301
        except ValueError as exc:
            loguru_logger.exception(
                "An error occurred",
                exc=exc,
                context={"additional": "info"},
            )

        logs = capture_logs.getvalue()
        assert (
            logs.strip()
            == "{'message': 'An error occurred', 'context': {'exception_type': 'ValueError', 'exception_message': 'Sample exception', 'additional': 'info'}}"  # noqa: E501
        )

    def test_logger_level_change(self, capture_logs: io.StringIO) -> None:
        """Test that debug messages are not logged at INFO level."""
        logger_info = LoguruLogger(level=LogLevel.INFO)
        logger_info.debug("This should not appear")
        assert not capture_logs.getvalue()

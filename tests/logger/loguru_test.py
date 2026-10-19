import json
from collections.abc import Iterator, Mapping
from types import MappingProxyType
from typing import Any

import pytest
from loguru import logger

from src.logger.loglevel import LogLevel
from src.logger.loguru import LoguruLogger


class TestLoguruLogger:
    """Test suite for Loguru logger."""

    @pytest.fixture(autouse=True)
    def remove_handlers(self) -> Iterator[None]:
        """Detach handlers bound to the test's captured stderr, closed after the test.

        Yields:
            Control to the test.
        """
        yield
        logger.remove()

    @pytest.mark.parametrize(
        ("level", "message", "context"),
        [
            ("debug", "Debug message", {"key": "value"}),
            ("info", "Info message", None),
            ("warning", "Warning message", {"key": "value"}),
            ("error", "Error message", {"error": "value"}),
            ("critical", "Critical message", None),
            ("info", "Proxy context", MappingProxyType({"key": "value"})),
        ],
    )
    def test_log_levels(
        self,
        capsys: pytest.CaptureFixture[str],
        level: str,
        message: str,
        context: Mapping[str, Any] | None,
    ) -> None:
        """Test all logging levels with various message/context combinations.

        Args:
            capsys: Captured stderr
            level: Log level to test
            message: Message to log
            context: Optional context dictionary
        """
        # Get logging method dynamically
        log_method = getattr(LoguruLogger(level=LogLevel.DEBUG), level)

        # Log with or without context
        log_method(message, context=context)

        # Get logged output
        log = json.loads(capsys.readouterr().err)
        record = log["record"]

        assert "\x1b" not in log["text"]
        assert record["level"]["name"] == level.upper()
        assert record["message"] == message
        assert record["extra"]["context"] == context
        assert record["function"] == "test_log_levels"

    def test_exception_log(
        self,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """Test exception logging with context.

        The test verifies that:
            - Exception message is properly logged
            - Exception type is included
            - Additional context is preserved
        """
        try:
            msg = "Sample exception"
            raise ValueError(msg)  # noqa: TRY301
        except ValueError as exc:
            LoguruLogger(level=LogLevel.DEBUG).exception(
                "An error occurred",
                exc=exc,
                context={"additional": "info"},
            )

        record = json.loads(capsys.readouterr().err)["record"]
        assert record["message"] == "An error occurred"
        assert record["level"]["name"] == "ERROR"
        assert record["function"] == "test_exception_log"
        assert record["extra"]["context"] == {
            "exception_type": "ValueError",
            "exception_message": "Sample exception",
            "additional": "info",
        }

    def test_logger_level_change(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test that debug messages are not logged at INFO level."""
        logger_info = LoguruLogger(level=LogLevel.INFO)
        logger_info.debug("This should not appear")
        assert not capsys.readouterr().err

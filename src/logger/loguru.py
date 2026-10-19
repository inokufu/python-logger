import sys
from collections.abc import Mapping
from typing import Any, override

from loguru import logger

from .contract import LoggerContract
from .loglevel import LogLevel


class LoguruLogger(LoggerContract):
    """Loguru implementation of the logger contract.

    Produces logs in a structured JSON format.
    """

    def __init__(self, level: LogLevel) -> None:
        """Initialize the Loguru logger with default configuration.

        Args:
            level: The minimum log level to display.
        """
        self._logger = logger
        self._logger.remove()

        self._logger.add(
            sink=sys.stderr,
            level=level,
            format="{time:%Y-%m-%d %H:%M:%S} | {level} | {message}",
            colorize=False,
            serialize=True,
            backtrace=level == LogLevel.DEBUG,  # Include full stack trace
            diagnose=level == LogLevel.DEBUG,  # Include variables in stack trace
        )

    def _log_with_context(
        self,
        level: LogLevel,
        message: str,
        context: Mapping[str, Any] | None = None,
    ) -> None:
        """Internal method to log messages with context.

        Args:
            level: The log level to use.
            message: The message to log.
            context: Additional contextual information to include with the log.
        """
        # depth=2: public methods must call this directly to attribute the caller
        self._logger.opt(depth=2).bind(
            context=dict(context) if context is not None else None,
        ).log(level.name, message)

    @override
    def debug(self, message: str, context: Mapping[str, Any] | None = None) -> None:
        self._log_with_context(level=LogLevel.DEBUG, message=message, context=context)

    @override
    def info(self, message: str, context: Mapping[str, Any] | None = None) -> None:
        self._log_with_context(level=LogLevel.INFO, message=message, context=context)

    @override
    def warning(self, message: str, context: Mapping[str, Any] | None = None) -> None:
        self._log_with_context(level=LogLevel.WARNING, message=message, context=context)

    @override
    def error(self, message: str, context: Mapping[str, Any] | None = None) -> None:
        self._log_with_context(level=LogLevel.ERROR, message=message, context=context)

    @override
    def critical(self, message: str, context: Mapping[str, Any] | None = None) -> None:
        self._log_with_context(
            level=LogLevel.CRITICAL,
            message=message,
            context=context,
        )

    @override
    def exception(
        self,
        message: str,
        exc: Exception,
        context: Mapping[str, Any] | None = None,
    ) -> None:
        exc_context = {
            "exception_type": type(exc).__name__,
            "exception_message": str(exc),
        }
        if context:
            exc_context.update(context)

        self._log_with_context(
            level=LogLevel.ERROR,
            message=message,
            context=exc_context,
        )

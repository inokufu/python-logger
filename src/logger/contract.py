from abc import ABC, abstractmethod
from collections.abc import Mapping
from typing import Any


class LoggerContract(ABC):
    """Abstract base class for logger implementations at various severity levels, with optional context information."""  # noqa: E501

    @abstractmethod
    def debug(self, message: str, context: Mapping[str, Any] | None = None) -> None:
        """Log a debug message.

        Args:
            message: The message to log
            context: Additional contextual information to include with the log.
        """
        raise NotImplementedError

    @abstractmethod
    def info(self, message: str, context: Mapping[str, Any] | None = None) -> None:
        """Log an info message.

        Args:
            message: The message to log
            context: Additional contextual information to include with the log.
        """
        raise NotImplementedError

    @abstractmethod
    def warning(self, message: str, context: Mapping[str, Any] | None = None) -> None:
        """Log a warning message.

        Args:
            message: The message to log
            context: Additional contextual information to include with the log.
        """
        raise NotImplementedError

    @abstractmethod
    def error(self, message: str, context: Mapping[str, Any] | None = None) -> None:
        """Log an error message.

        Args:
            message: The message to log
            context: Additional contextual information to include with the log.
        """
        raise NotImplementedError

    @abstractmethod
    def critical(self, message: str, context: Mapping[str, Any] | None = None) -> None:
        """Log a critical message.

        Args:
            message: The message to log
            context: Additional contextual information to include with the log.
        """
        raise NotImplementedError

    @abstractmethod
    def exception(
        self,
        message: str,
        exc: Exception,
        context: Mapping[str, Any] | None = None,
    ) -> None:
        """Log an exception.

        Args:
            message: A descriptive message about the exception
            exc: The exception object
            context: Additional contextual information to include with the log.
        """
        raise NotImplementedError

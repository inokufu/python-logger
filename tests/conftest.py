"""This file contains pytest fixtures available to all tests.

Fixtures are functions that pytest runs before tests to set up preconditions.
pytest automatically discovers this file and makes fixtures available
to all test modules without needing to import them.
"""

from unittest.mock import Mock

import pytest

from src.logger.contract import LoggerContract


@pytest.fixture
def mock_logger() -> Mock:
    """Create a mock logger.

    :return: A mock logger conforming to LoggerContract
    """
    return Mock(spec=LoggerContract)

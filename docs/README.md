# Logger

[![Python](https://img.shields.io/badge/Python-FFD43B?logo=python)](https://www.python.org/)
![License](https://img.shields.io/badge/GPL--3.0-red?logo=gnu)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-E6F0FF?logo=githubactions)](https://github.com/features/actions)
[![Pytest](https://img.shields.io/badge/pytest-E6F7FF?logo=pytest)](https://docs.pytest.org/)
[![EditorConfig](https://img.shields.io/badge/EditorConfig-333333?logo=editorconfig)](https://editorconfig.org/)
[![Rye](https://img.shields.io/badge/Rye-000000?logo=rye)](https://rye.astral.sh/)
[![Ruff](https://img.shields.io/badge/Ruff-3A3A3A?logo=ruff)](https://docs.astral.sh/ruff/)
[![Pre-commit](https://img.shields.io/badge/pre--commit-40332E?logo=pre-commit)](https://pre-commit.com/)
[![Makefile](https://img.shields.io/badge/Makefile-427819?logo=gnu)](https://www.gnu.org/software/make/manual/make.html)
[![MkDocs](https://img.shields.io/badge/MkDocs-526CFE?logo=markdown)](https://www.mkdocs.org/)

## Overview

This project provides a flexible and extensible logging framework for Python
applications. It offers a clean interface for consistent logging with rich
context information, built on top of the Loguru library while maintaining a
contract-based approach for easy adaptation to other logging backends.

Key features:

- 📏 Standardized logging interface through a contract
- 🔄 Easy integration into existing classes via a mixin
- 🌈 Beautiful, colorized console output via Loguru
- 🧩 Structured logging with context support
- 📊 Granular log level control
- 🧪 Thoroughly tested implementation

## Setup and installation

### Prerequisites

- Python 3.12 or higher
- [Rye](https://rye.astral.sh) for dependency management

### Installation

1. Clone the repository

2. Install dependencies
   ```sh
   make init
   ```

## Usage

### Basic Usage

```python
# Create a logger instance
logger = LoguruLogger(level=LogLevel.DEBUG)

# Basic logging
logger.info("Application started")

# Logging with context
logger.debug("Processing item",
             context={"item_id": "12345", "status": "pending"})

# Error logging
try:
    result = 1 / 0
except Exception as e:
    logger.exception("Division error occurred", exc=e,
                     context={"operation": "division"})
```

### Using the LoggableMixin

```python
# Create a class with logging capabilities
class MyService(LoggableMixin):
    def __init__(self, logger: LoggerContract):
        super().__init__()
        self.logger = logger

    def process(self, data):
        self.logger.info("Processing data", context={"data_size": len(data)})


# Usage
logger = LoguruLogger(level=LogLevel.INFO)
service = MyService(logger)
service.process([1, 2, 3])
```

### Log Levels

Available log levels (from lowest to highest priority):

- `LogLevel.DEBUG` - Detailed information for debugging
- `LogLevel.INFO` - General information about system operation
- `LogLevel.WARNING` - Indication of potential issues
- `LogLevel.ERROR` - Error conditions preventing a function from working
- `LogLevel.CRITICAL` - Critical conditions requiring immediate attention

Set the log level when creating the logger:

```python
# Only show warnings and above
logger = LoguruLogger(level=LogLevel.WARNING)
```

## API Reference

### LoggerContract

The abstract base class that defines the interface for all logger
implementations:

| Method                                  | Description                                     |
|-----------------------------------------|-------------------------------------------------|
| `debug(message, context=None)`          | Log debug message with optional context         |
| `info(message, context=None)`           | Log info message with optional context          |
| `warning(message, context=None)`        | Log warning message with optional context       |
| `error(message, context=None)`          | Log error message with optional context         |
| `critical(message, context=None)`       | Log critical message with optional context      |
| `exception(message, exc, context=None)` | Log exception with message and optional context |

### LoguruLogger

An implementation of `LoggerContract` using
the [Loguru](https://github.com/Delgan/loguru) library.

### LoggableMixin

A mixin class that adds logging capabilities to any class.

| Property | Description                    |
|----------|--------------------------------|
| `logger` | Get or set the logger instance |

### LogLevel

An enum representing log levels:

- `DEBUG`
- `INFO`
- `WARNING`
- `ERROR`
- `CRITICAL`

With a helper method:

- `from_str(value)` - Create LogLevel from a string (case-insensitive)

## Development

### Code Formatting and Linting

This project uses ruff for formatting and linting:

```sh
# Format code
make format

# Run linters
make lint
```

### Running Tests

```sh
# Run tests with coverage
make test
```

## Contributing

We welcome contributions to this project! Please see
the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to
contribute, including:

- How to set up your development environment
- Coding standards and style guidelines
- Pull request process
- Testing requirements

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0) -
see the LICENSE file for details.

GPL-3.0 is a strong copyleft license that requires anyone who distributes your
code or a derivative work to make the source available under the same terms.

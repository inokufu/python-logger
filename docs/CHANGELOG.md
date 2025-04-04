# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-03-20

### Added

- Initial release of the logging framework
- `LoggerContract` abstract base class defining the logger interface
- `LoguruLogger` implementation using Loguru library
- `LogLevel` enum for standardized log levels
- `LoggableMixin` for adding logging capabilities to classes
- Comprehensive test suite for all components
- Support for structured logging with context information
- Exception logging with type and message extraction

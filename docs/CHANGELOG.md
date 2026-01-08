# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2026-01-06

### Changed

- Python version to 3.14
- Migrated from Rye to uv
- Type checking with ty

## [0.2.0] - 2025-07-17

### Changed

- Python version to 3.13
- Upgrade dependencies

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

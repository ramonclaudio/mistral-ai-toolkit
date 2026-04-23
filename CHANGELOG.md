# Changelog

All notable changes to the project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v1.1.0] - [03/28/2024]

- *v1.1.0 introduces a major change removing the use of `httpx` & `asyncio` and implementing `requests`, making it more accessible.*

### Added
- Default model configuration in `config.py` for fallback model specification.

### Changed
- Loading spinner implementation in `loading.py` to use threading instead of asyncio.
- Refactored `mistral.py` into two separate classes for different types of interactions.
- Switched HTTP client library from `httpx` to `requests` in `client.py`.
- Updated CLI argument parser and help text in `cli.py` to reflect the new functionalities and simplifications.

### Improved
- Error messaging in `config.py` for missing environment variables or missing `dotenv` package.
- Response formatting in `client.py` to handle newline characters correctly.

### Fixed
- Handling of newline characters in responses for better output formatting in `client.py`.

## [1.0.0] - 03/01/2024

### Added
- Initial release.

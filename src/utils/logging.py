import logging
import sys
from typing import Optional


def setup_logging(
    log_file: Optional[str] = None, level: int = logging.INFO
) -> logging.Logger:
    """
    Set up logging configuration for the application.

    Args:
        log_file: Path to the log file. If None, logs will only be printed to the console.
        level: Logging level (e.g., logging.DEBUG, logging.INFO).

    Returns:
        Configured logger instance.

    Raises:
        PermissionError: If the log file cannot be written due to permission issues.
        OSError: If the log file path is invalid or the file cannot be created.

    Examples:
        >>> logger = setup_logging()
        >>> logger = setup_logging(log_file="app.log", level=logging.DEBUG)
    """
    logger = logging.getLogger("2DGameEditor")
    logger.setLevel(level)

    # Clear any existing handlers to avoid duplicate logs
    logger.handlers.clear()

    # Create a formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Add console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Add file handler if log_file is provided
    if log_file:
        try:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except PermissionError as e:
            logger.error(f"Permission denied while setting up log file: {e}")
            raise
        except OSError as e:
            logger.error(f"Error setting up log file: {e}")
            raise

    return logger

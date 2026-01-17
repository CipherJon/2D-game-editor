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
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

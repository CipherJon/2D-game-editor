"""
Utility functions for secure file operations.
This module provides functions for validating file paths, ensuring secure file handling, and managing file permissions.
"""

import os
from typing import Optional, Tuple


def validate_file_path(file_path: str) -> bool:
    """
    Validate a file path to ensure it is safe and within the allowed directory.

    Args:
        file_path (str): The file path to validate.

    Returns:
        bool: True if the file path is valid, False otherwise.

    Raises:
        ValueError: If the file path is invalid or unsafe.

    Examples:
        >>> validate_file_path("resources/image.png")
        True
        >>> validate_file_path("../../../etc/passwd")
        False
    """
    if not isinstance(file_path, str):
        raise ValueError("File path must be a string.")

    # Check for path traversal attempts
    if ".." in file_path or file_path.startswith("/"):
        raise ValueError("File path contains unsafe characters.")

    # Check if the file path is within the allowed directory
    allowed_dir = "resources"
    if not file_path.startswith(allowed_dir):
        raise ValueError(f"File path must be within the '{allowed_dir}' directory.")

    return True


def ensure_directory_exists(directory_path: str) -> None:
    """
    Ensure that a directory exists, creating it if necessary.

    Args:
        directory_path (str): The path to the directory.

    Raises:
        PermissionError: If the directory cannot be created due to permission issues.
        OSError: If the directory path is invalid or cannot be created.

    Examples:
        >>> ensure_directory_exists("resources/cache")
    """
    try:
        os.makedirs(directory_path, exist_ok=True)
    except PermissionError as e:
        raise PermissionError(f"Permission denied while creating directory: {e}")
    except OSError as e:
        raise OSError(f"Error creating directory: {e}")


def get_file_permissions(file_path: str) -> Optional[Tuple[bool, bool, bool]]:
    """
    Get the read, write, and execute permissions for a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        Optional[Tuple[bool, bool, bool]]: A tuple of (readable, writable, executable) permissions, or None if the file does not exist.

    Raises:
        PermissionError: If the file permissions cannot be checked due to permission issues.

    Examples:
        >>> get_file_permissions("resources/image.png")
        (True, True, False)
    """
    if not os.path.exists(file_path):
        return None

    try:
        readable = os.access(file_path, os.R_OK)
        writable = os.access(file_path, os.W_OK)
        executable = os.access(file_path, os.X_OK)
        return (readable, writable, executable)
    except PermissionError as e:
        raise PermissionError(f"Permission denied while checking file permissions: {e}")


def secure_file_write(file_path: str, content: str) -> None:
    """
    Securely write content to a file, ensuring the file path is valid and the directory exists.

    Args:
        file_path (str): The path to the file.
        content (str): The content to write to the file.

    Raises:
        ValueError: If the file path is invalid or unsafe.
        PermissionError: If the file cannot be written due to permission issues.
        OSError: If the file path is invalid or the file cannot be created.

    Examples:
        >>> secure_file_write("resources/config.txt", "key=value")
    """
    validate_file_path(file_path)
    directory_path = os.path.dirname(file_path)
    ensure_directory_exists(directory_path)

    try:
        with open(file_path, "w") as file:
            file.write(content)
    except PermissionError as e:
        raise PermissionError(f"Permission denied while writing to file: {e}")
    except OSError as e:
        raise OSError(f"Error writing to file: {e}")


def secure_file_read(file_path: str) -> Optional[str]:
    """
    Securely read content from a file, ensuring the file path is valid and the file exists.

    Args:
        file_path (str): The path to the file.

    Returns:
        Optional[str]: The content of the file, or None if the file does not exist.

    Raises:
        ValueError: If the file path is invalid or unsafe.
        PermissionError: If the file cannot be read due to permission issues.
        OSError: If the file path is invalid or the file cannot be read.

    Examples:
        >>> secure_file_read("resources/config.txt")
        "key=value"
    """
    validate_file_path(file_path)

    if not os.path.exists(file_path):
        return None

    try:
        with open(file_path, "r") as file:
            return file.read()
    except PermissionError as e:
        raise PermissionError(f"Permission denied while reading file: {e}")
    except OSError as e:
        raise OSError(f"Error reading file: {e}")

"""
Exceptions for the goodman project.
"""


class BaseGoodmanException(Exception):
    """Base Exception that all Exceptions inherit from."""
    pass


class MalformedArgument(BaseGoodmanException):
    """Exception raised when an argument passed into a method is malformed."""
    pass


class DeadProperty(BaseGoodmanException):
    """Exception passed when an unused property is accessed."""

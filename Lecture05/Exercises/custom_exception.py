class Error(Exception):
    """Base class for errors in this module."""
    pass

class BadLoginError(Error):
    """A user attempted to login with
    an incorrect password."""
    pass

    
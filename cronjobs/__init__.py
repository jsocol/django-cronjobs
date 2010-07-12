registered = {
    'weekly': {},
    'daily': {},
    'hourly': {},
    'minutely': {},
    'others': {},
}


def register(rate='others'):
    """Decorator to add the function to the cronjob library."""
    def decorator(f):
        registered[rate][f.__name__] = f
        return f
    return decorator

registered = {}
registered_lock = {}

def register(f=None, lock=True):
    """Decorator to add the function to the cronjob library.

        @cronjobs.register
        def my_task():
            print('I can be run once/machine at a time.')

        @cronjobs.register(lock=False)
        def my_task():
            print('I am concurrent friendly!')

    """

    def decorator(f, lock=lock):
        registered[f.__name__] = f
        if lock:
            registered_lock[f.__name__] = f
        return f

    if callable(f):
        return decorator(f, lock)
    return decorator

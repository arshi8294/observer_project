from functools import wraps


def observer_decorator(func):
    @wraps(func)
    def wrapper(obj, *args, **kwargs):
        func(obj, *args, **kwargs)
        for observer in obj.observers:
            observer.update(obj.state)

    return wrapper


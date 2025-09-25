import inspect
from functools import wraps


def enforce_types(func):
    sig = inspect.signature(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)  # 按照解释器规则绑定
        bound.apply_defaults()             # 补上默认值

        for name, value in bound.arguments.items():
            expected_type = func.__annotations__.get(name)
            if expected_type and value is not None and not isinstance(value, expected_type):
                raise TypeError(f"Argument '{name}' must be {expected_type}, got {type(value).__name__}")
        return func(*bound.args, **bound.kwargs)

    return wrapper
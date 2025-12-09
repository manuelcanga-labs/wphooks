# Examples of filters functions usage

This document contains examples of how to use the filters functions.

## Basic Usage

You can add a filter using `add_filter` and apply it using `apply_filters`.

```python
from wphooks import add_filter, apply_filters

# Define a callback function
def my_callback(value):
    return value + 1

# Add the filter
add_filter("my_hook", my_callback)

# Apply the filter
result = apply_filters("my_hook", 10)
print(result) # Output: 11
```

## Using Decorators

You can also use the `@filter` decorator to register a function as a filter.

```python
from wphooks import filter, apply_filters

@filter("my_decorator_hook")
def my_decorator_callback(value):
    return value * 2

result = apply_filters("my_decorator_hook", 5)
print(result) # Output: 10
```

## Priority

Filters can have a priority. Lower numbers run earlier.

```python
from wphooks import add_filter, apply_filters

# Priority 10 (default)
add_filter("priority_hook", lambda x: x + "a", priority=10)

# Priority 5 (runs first)
add_filter("priority_hook", lambda x: x + "b", priority=5)

result = apply_filters("priority_hook", "start")
print(result) # Output: startba (start + b + a)
```

## Passing Arguments

You can pass multiple arguments to filters. Specify `accepted_args` when adding the filter.

```python
from wphooks import add_filter, apply_filters

def sum_args(a, b, c):
    return a + b + c

# Register filter accepting 3 arguments
add_filter("args_hook", sum_args, accepted_args=3)

# Apply filter with arguments
# 1 is the default value (a), 2 and 3 are additional arguments (b, c), 4 and 5 are ignored
result = apply_filters("args_hook", 1, 2, 3, 4, 5)
print(result) # Output: 6
```

## Handling Fewer Arguments

If the number of arguments passed to `apply_filters` is less than `accepted_args` specified in `add_filter`, the callback will be called with the available arguments.

```python
from wphooks import add_filter, apply_filters

def optional_args_callback(val, extra=None):
    if extra:
        return val + extra
    return val

# Register filter with accepted_args=2 (val + extra)
add_filter("optional_hook", optional_args_callback, accepted_args=2)

# Apply with extra argument
print(apply_filters("optional_hook", "Value", "Extra")) # Output: ValueExtra

# Apply without extra argument
print(apply_filters("optional_hook", "Value")) # Output: Value
```

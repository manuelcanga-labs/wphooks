# Examples of actions functions usage

This document contains examples of how to use the actions functions.

## Basic Usage

You can add an action using `add_action` and execute it using `do_action`.

```python
from wphooks import add_action, do_action

# Define a callback function
def my_callback(value):
    print(f"Action executed with value: {value}")

# Add the action
add_action("my_hook", my_callback)

# Do the action
do_action("my_hook", 10) # Output: Action executed with value: 10
```

## Using Decorators

You can also use the `@action` decorator to register a function as an action.

```python
from wphooks import action, do_action

@action("my_decorator_hook")
def my_decorator_callback(value):
    print(f"Decorator action executed with value: {value}")

do_action("my_decorator_hook", 5) # Output: Decorator action executed with value: 5
```

## Priority

Actions can have a priority. Lower numbers run earlier.

```python
from wphooks import add_action, do_action

# Priority 10 (default)
add_action("priority_hook", lambda x: print(f"{x} Second"), priority=10)

# Priority 5 (runs first)
add_action("priority_hook", lambda x: print(f"{x} First"), priority=5)

do_action("priority_hook", "Sequence:")
# Output:
# Sequence: First
# Sequence: Second
```

## Passing Arguments

You can pass multiple arguments to actions. Specify `accepted_args` when adding the action.

```python
from wphooks import add_action, do_action

def sum_args(a, b, c):
    print(f"Sum: {a + b + c}")

# Register action accepting 3 arguments
add_action("args_hook", sum_args, accepted_args=3)

# Do action with arguments
# 1 is the first argument (a), 2 and 3 are additional arguments (b, c), 4 and 5 are ignored
do_action("args_hook", 1, 2, 3, 4, 5) # Output: Sum: 6
```

## Actions Without Arguments

You can also define and trigger actions that take no arguments by setting `accepted_args=0`.

```python
from wphooks import add_action, do_action

def no_args_callback():
    print("Executed without arguments!")

# Register action with accepted_args=0
add_action("no_args_hook", no_args_callback, accepted_args=0)

# Trigger the action without arguments
do_action("no_args_hook") 
# Output: Executed without arguments!
```


## Handling Fewer Arguments

If the number of arguments passed to `do_action` is less than `accepted_args` specified in `add_action`, the callback will be called with the available arguments.

```python
from wphooks import add_action, do_action

def optional_args_callback(a=None, b=None):
    if a and b:
        print(f"Called with {a} and {b}")
    elif a:
        print(f"Called with {a}")
    else:
        print("Called with no arguments")

# Register action with accepted_args=2
add_action("optional_hook", optional_args_callback, accepted_args=2)

# Trigger with 2 arguments
do_action("optional_hook", 1, 2) # Output: Called with 1 and 2

# Trigger with 1 argument
do_action("optional_hook", 1) # Output: Called with 1

# Trigger with 0 arguments (only hook name)
do_action("optional_hook") # Output: Called with no arguments
```

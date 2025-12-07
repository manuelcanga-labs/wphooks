# WPHooks: WordPress-style Hooks for Python

**WPHooks** is a lightweight Python library that brings the powerful Event-Driven Architecture of WordPress—Actions and
Filters—to your Python projects. It allows you to create extensible, modular, and plugin-friendly applications with
ease.

## Why WPHooks?

WordPress's hook system is a proven pattern for building flexible software. It allows developers to "hook" into specific
points of the application execution to modify data or add custom functionality without altering the core codebase.
`wphooks` implements this exact behavior in Python.

### Perfect for Legacy Projects

Refactoring legacy code ("spaghetti code") is often risky and difficult. `wphooks` offers a strategic way to modernize
these projects:

1. **Open/Closed Principle**: You can extend the functionality of a legacy function without modifying its internal
   logic.
2. **Safe Injection**: Instead of rewriting a massive function to add a new feature, you can simply trigger an action or
   apply a filter at the key point.
3. **Decoupling**: New features implementation stays in separate files/modules, keeping the old codebase clean and
   untouched.

**Example Scenario**:
Imagine a 1000-line function `process_order()` that is critical to your business. You need to add a "Send Slack
Notification" feature. Instead of risking a bug by editing `process_order()`, you just add
`do_action('order_processed', order_id)` at the end. Your new Slack logic lives in a completely new file, hooked to
`order_processed`.

## Installation

*(Assuming this will be a package or just added to the project)*

```python
from wphooks import add_action, do_action
from wphooks import add_filter, apply_filters
```

## Concepts

There are two main types of hooks:

1. **Actions**: "Do something". They are events that trigger when something happens. They don't return a value. (e.g., "
   User registered", "Page loaded").
2. **Filters**: "Modify something". They accept a value, modify it, and return it. (e.g., "Format title", "Calculate
   total price").

---

## Actions

Actions allow you to execute custom code at specific points in your execution flow.

### Basic Example

```python
from wphooks import add_action, do_action


# 1. Define your custom function
def send_welcome_email(user_id):
    print(f"Sending welcome email to user {user_id}...")


# 2. Hook your function to an action name
add_action('user_registered', send_welcome_email)

# 3. Trigger the action somewhere in your code
# This will execute all functions hooked to 'user_registered'
do_action('user_registered', 123)
# Output: Sending welcome email to user 123...
```

**[See more Action examples and detailed usage](./examples/actions.md)**

---

## Filters

Filters allow you to intercept data, modify it, and pass it back.

### Basic Example

```python
from wphooks import add_filter, apply_filters


# 1. Define your filter function
# It receives a value (and optional args), and MUST return a value
def make_title_uppercase(title):
    return title.upper()


# 2. Hook your function to a filter name
add_filter('the_title', make_title_uppercase)

# 3. Apply the filter to your data
title = "hello world"
filtered_title = apply_filters('the_title', title)

print(filtered_title)
# Output: HELLO WORLD
```

**[See more Filter examples and detailed usage](./examples/filters.md)**

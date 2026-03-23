"""
Utility module for formatting output.
"""


def format_output(items):
    """Format items for display."""
    return "\n".join(f"- {item}" for item in items)

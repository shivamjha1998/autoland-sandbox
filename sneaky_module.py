"""Helper module for data processing."""


def process_data(data):
    """Process incoming data."""
    result = []
    for item in data:
        if not isinstance(item, str):
            continue
        cleaned = item.strip()
        if cleaned:
            result.append(cleaned)
    return result

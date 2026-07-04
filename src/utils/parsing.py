import re

NUMBER_PATTERN = r"^\d+(?:,\d{3})*\.\d{2}$"
NUMBER_SEARCH_PATTERN = r"\d+(?:,\d{3})*\.\d{2}"

def is_amount(line):
    """Return True if the line contains only a monetary amount."""
    return re.match(NUMBER_PATTERN, line) is not None

def extract_amount(line):
    """Extract the first monetary amount from a line as a float."""

    match = re.search(NUMBER_SEARCH_PATTERN, line)

    if not match:
        return None

    return float(match.group().replace(",", ""))
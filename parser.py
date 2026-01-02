import re
from datetime import datetime

LOG_PATTERN = re.compile(
        r"""
        (?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})  # Timestamp in YYYY-MM-DD HH:MM:SS format
        \s+
        (?P<log_level>INFO|DEBUG|WARNING|ERROR|CRITICAL)    # Log level
        \s+
        (?P<service>[A-Za-z0-9_]+)                           # Service name
        \s+
        (?P<message>.+)                                     # Log message
        """,
        re.VERBOSE
    )


def parse_log_line(line):
    if not line or not isinstance(line, str):
        raise ValueError("Input line must be a non-empty string")
    try:
        match = LOG_PATTERN.match(line)
        if not match:
            raise ValueError("Log line does not match expected format")

        log_data = match.groupdict()
        log_data['timestamp'] = datetime.strptime(log_data['timestamp'], '%Y-%m-%d %H:%M:%S')
        return log_data
    except Exception as e:
        raise ValueError(f"Failed to parse log line: {e}")

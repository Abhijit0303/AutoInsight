from datetime import datetime
import re

LOG_PATTERN = re.compile(
    r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) '
    r'(INFO|ERROR|WARNING) '
    r'(\S+) '
    r'(.+)$'
)

def parse_log_line(line):

    #I am returning None because I don't want the pipeline should break in the meantime
    if not line:
        return None

    match = LOG_PATTERN.match(line)
    if not match:
        return None

    timestamp_str, level, service, message = match.groups()

    try:
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None

    return {
        "timestamp": timestamp,
        "level": level,
        "service": service,
        "message": message.strip()
    }

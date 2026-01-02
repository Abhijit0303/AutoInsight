from collections import defaultdict

def analyzer_logs(parsed_logs):
    stats = {
        "total_logs": 0,
        "levels": defaultdict(int),
        "services": defaultdict(int),
        "errors_by_service": defaultdict(int),
        "errors_by_hour": defaultdict(int),
    }

    for log in parsed_logs:
        stats["total_logs"] += 1

        level = log.get("log_level")
        service = log.get("service")
        timestamp = log.get("timestamp")

        if level:
            stats["levels"][level] += 1
        if service:
            stats["services"][service] += 1
        if level == "ERROR" and timestamp:
            hour_bucket = timestamp.strftime('%Y-%m-%d %H:00:00')
            stats["errors_by_hour"][hour_bucket] += 1

            if service:
                stats["errors_by_service"][service] += 1

    return stats
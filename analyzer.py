from collections import defaultdict

def analyzer_logs(parsed_logs):
    stats = {
        "total_logs": 0,
        "levels": defaultdict(int),
        "services": defaultdict(int),
        "errors_by_hour": defaultdict(int),
        "errors_by_service": defaultdict(int),
    }

    for log in parsed_logs:
        stats["total_logs"] += 1

        level = log.get("level")
        service = log.get("service")
        timestamp = log.get("timestamp")

        # COUNT LEVELS
        if level is not None:
            stats["levels"][level] += 1

        # Count logs per service (all levels)
        if service is not None:
            stats["services"][service] += 1

        # ERROR-specific metrics
        if level == "ERROR" and timestamp is not None:
            hour_bucket = timestamp.strftime("%Y-%m-%d %H:00")
            stats["errors_by_hour"][hour_bucket] += 1

            if service is not None:
                stats["errors_by_service"][service] += 1

    return stats

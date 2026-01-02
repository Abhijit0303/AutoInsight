from statistics import mean

def detect_error_spikes(error_by_hour, threshold=2.0):
    if not error_by_hour or not isinstance(error_by_hour, dict):
        return []

    error_counts = list(error_by_hour.values())

    if len(error_counts) < 3:
        return []

    baseline_avg = mean(error_counts)

    anomalies = []
    for hour, count in error_by_hour.items():
        if count > baseline_avg * threshold:
            anomalies.append(
                    {
                        "hour": hour,
                        "error_count": count,
                        "baseline_avg": round(baseline_avg, 2)
                    }
                )

    return anomalies

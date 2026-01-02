import os
import json
from datetime import datetime

REPORT_DIR = "reports"

def ensure_report_dir():
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)

def generate_text_report(stats, anomalies):
    ensure_report_dir()
    report_path = os.path.join(REPORT_DIR, 'log_report.txt')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    lines = []
    lines.append(f"Log Analysis Report - Generated on {timestamp}\n")
    lines.append("Overall Statistics:")
    lines.append("=" * 10)
    lines.append(f"Total Log Entries: {stats.get('total_logs', 0)}")
    lines.append(f"\nERROR logs : {stats.get('levels', {}).get('ERROR', 0)}")
    lines.append(f"\nWARNING logs : {stats.get('levels', {}).get('WARNING', 0)}")
    lines.append("\n")

    lines.append("ERRORS BY SERVICE")
    lines.append("-" * 20)

    services = stats.get('errors_by_service', {})
    if services:
        for service, count in sorted(services.items(), key=lambda x: x[1], reverse=True):
            lines.append(f"{service:20}: {count}")

    else:
        lines.append("No ERROR logs found for any service.")

    lines.append("\nANOMALIES DETECTED")
    lines.append("-" * 20)
    if anomalies:
        for anomaly in anomalies:
            lines.append(
                f"Hour: {anomaly['hour']}"
                f"Error Count: {anomaly['error_count']}"
                f"Baseline Avg: {anomaly['baseline_avg']}"
            )
    else:
        lines.append("No anomalies detected.")

    with open(report_path, 'w') as f:
        f.write('\n'.join(lines))

def generate_json_report(stats, anomalies):
    ensure_report_dir()
    report_path = os.path.join(REPORT_DIR, 'log_report.json')
    report_data = {
        "generated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "summary": {
            "total_logs": stats.get('total_logs', 0),
            "levels": dict(stats.get('levels', {})),
        },
        "errors_by_service": dict(stats.get('errors_by_service', {})),
        "errors_by_hour": dict(stats.get('errors_by_hour', {})),
        "anomalies": anomalies
    }

    with open(report_path, 'w') as f:
        json.dump(report_data, f, indent=4)
import os
import matplotlib.pyplot as plt

REPORT_DIR = "reports"

def ensure_report_dir():
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)

def plot_errors_by_hour(errors_by_hour):
    if not errors_by_hour:
        print("No error data to plot.")
        return

    ensure_report_dir()

    hours = sorted(errors_by_hour.keys())
    error_counts = [errors_by_hour[hour] for hour in hours]

    plt.figure()
    plt.plot(hours, error_counts, marker='o')
    plt.xticks(rotation=45)
    plt.xlabel('Time (Hour)')
    plt.ylabel('Number of Errors')
    plt.title('Errors by Hour')
    plt.tight_layout()
    plt.savefig(os.path.join(REPORT_DIR, 'errors_by_hour.png'))
    plt.close()

def plot_errors_by_service(errors_by_service):
    if not errors_by_service:
        print("No error data to plot.")
        return

    ensure_report_dir()

    services = list(errors_by_service.keys())
    error_counts = [errors_by_service[service] for service in services]

    plt.figure()
    plt.bar(services, error_counts)
    plt.xlabel('Service')
    plt.ylabel('Number of Errors')
    plt.title('Errors by Service')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(REPORT_DIR, 'errors_by_service.png'))
    plt.close()

def plot_log_levels(levels):
    if not levels:
        print("No log level data to plot.")
        return

    ensure_report_dir()

    log_levels = list(levels.keys())
    counts = [levels[level] for level in log_levels]

    plt.figure()
    plt.bar(log_levels, counts, color=['green', 'blue', 'orange', 'red', 'purple'])
    plt.xlabel('Log Level')
    plt.ylabel('Count')
    plt.title('Log Levels Distribution')
    plt.tight_layout()
    plt.savefig(os.path.join(REPORT_DIR, 'log_levels_distribution.png'))
    plt.close()
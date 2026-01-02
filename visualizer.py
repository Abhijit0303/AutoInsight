import os
import matplotlib.pyplot as plt

REPORT_DIR = "reports"


def _ensure_report_dir():
    os.makedirs(REPORT_DIR, exist_ok=True)


def plot_errors_by_hour(errors_by_hour):
    if not isinstance(errors_by_hour, dict) or len(errors_by_hour) == 0:
        return

    _ensure_report_dir()

    hours = sorted(errors_by_hour.keys())
    counts = [errors_by_hour[h] for h in hours]

    plt.figure()
    plt.plot(hours, counts, marker="o")
    plt.title("Errors per Hour")
    plt.xlabel("Hour")
    plt.ylabel("Error Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{REPORT_DIR}/errors_by_hour.png")
    plt.close()


def plot_errors_by_service(errors_by_service):
    if not isinstance(errors_by_service, dict) or len(errors_by_service) == 0:
        return

    _ensure_report_dir()

    services = list(errors_by_service.keys())
    counts = list(errors_by_service.values())

    plt.figure()
    plt.bar(services, counts)
    plt.title("Errors by Service")
    plt.xlabel("Service")
    plt.ylabel("Error Count")
    plt.tight_layout()
    plt.savefig(f"{REPORT_DIR}/errors_by_service.png")
    plt.close()


def plot_log_levels(levels):
    if not isinstance(levels, dict) or len(levels) == 0:
        return

    _ensure_report_dir()

    labels = list(levels.keys())
    sizes = list(levels.values())

    plt.figure()
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.title("Log Level Distribution")
    plt.tight_layout()
    plt.savefig(f"{REPORT_DIR}/log_level_distribution.png")
    plt.close()

from parser import parse_log_line
from analyzer import analyzer_logs
from detector import detect_error_spikes
from reporter import generate_text_report, generate_json_report
from visualizer import plot_errors_by_hour, plot_errors_by_service, plot_log_levels

LOG_FILE_PATH = 'logs/server.log'

def main():
    parsed_logs = []

    try:
        with open(LOG_FILE_PATH, 'r') as log_file:
            for line in log_file:
                parsed = parse_log_line(line.rstrip("\n"))
                if parsed:
                    parsed_logs.append(parsed)
                # print("PARSED SAMPLE:", parsed_logs[:3])

    except FileNotFoundError:
        print(f"Log file not found: {LOG_FILE_PATH}")
        return
    except Exception as e:
        print(f"Error reading log file: {e}")
        return

    if not parsed_logs:
        print("No valid log entries found.")
        return

    stats = analyzer_logs(parsed_logs)

    anamolies = detect_error_spikes(stats.get('errors_by_hour', 0))

    plot_errors_by_hour(stats.get('errors_by_hour', {}))
    plot_errors_by_service(stats.get('errors_by_service', {}))
    plot_log_levels(stats.get('levels', {}))

    generate_text_report(stats, anamolies)
    generate_json_report(stats, anamolies)

    print("Log analysis complete. Reports and visualizations generated." \
    "" \
    " Check the 'reports' directory.")


if __name__ == "__main__":
    main()


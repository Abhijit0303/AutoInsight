# AutoInsight 🔍

**Python Log Analysis & Incident Detection Tool**

AutoInsight is a production-style log analysis pipeline built using pure Python.
It parses raw server logs, extracts insights, detects anomalies, and generates
persistent reports and visualizations.

---

## 🚀 Features

- Parses raw, unstructured server log files
- Converts logs into structured data
- Generates analytics and statistics
- Detects abnormal error spikes
- Produces visual insights (PNG graphs)
- Generates human-readable and machine-readable reports
- Modular, maintainable codebase
- Framework-free (no pandas, no web frameworks)

---

## 🧠 Design Philosophy

> Unstructured text → Structured data → Insights → Artifacts

Each module has a single responsibility, closely mirroring real backend and SRE
tooling used in production systems.

---

## 📁 Project Structure

```
autoinsight/
│── main.py          # Pipeline orchestration
│── parser.py        # Defensive log parsing
│── analyzer.py      # Aggregation & analytics
│── detector.py      # Anomaly detection logic
│── visualizer.py    # Visualization generation
│── reporter.py      # Report generation
│── logs/
│   └── server.log   # Input log file
│── reports/
│   ├── incident_report.txt
│   ├── incident_report.json
│   ├── errors_by_hour.png
│   ├── errors_by_service.png
│   └── log_level_distribution.png
│── requirements.txt
│── LICENSE
│── README.md
```

---

## 📌 Supported Log Format

Each log entry must follow the format:

```
YYYY-MM-DD HH:MM:SS LEVEL ServiceName Message
```

### Example

```
2025-01-01 00:00:00 ERROR AuthService Authentication failed
```

Supported log levels:

- INFO
- WARNING
- ERROR

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/autoinsight.git
cd autoinsight
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate    # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### 1. Add your log file

Place your log file at:

```
logs/server.log
```

### 2. Run the pipeline

```bash
python main.py
```

### 3. View outputs

All generated artifacts will appear in the `reports/` directory.

---

## 📊 Outputs Generated

### Reports

- `incident_report.txt` – Human-readable summary
- `incident_report.json` – Machine-readable structured report

### Visualizations

- Errors per hour (line chart)
- Errors by service (bar chart)
- Log level distribution (pie chart)

---

## 🚨 Anomaly Detection

AutoInsight uses a deterministic and explainable approach:

- Calculates baseline average error rate
- Flags hours exceeding a configurable threshold
- No machine learning involved

---

## 🧪 Reliability & Robustness

- Malformed log lines are safely ignored
- Parser never crashes the pipeline
- Defensive checks across all modules
- Consistent output even with partial data

---

## 🧰 Tech Stack

- **Language:** Python
- **Dependencies:** Listed in `requirements.txt`
- **Visualization:** matplotlib

Concepts demonstrated:

- File I/O
- Regex parsing
- Datetime handling
- Data aggregation
- Modular architecture
- Anomaly detection
- Pipeline orchestration

---

## 📈 Future Improvements

- CLI arguments using `argparse`
- Config-driven thresholds
- CSV export support
- HTML / PDF reports
- Streaming log ingestion
- Integration with monitoring systems

---

## 📜 License

This project is licensed under the terms defined in the `LICENSE` file included
in this repository.

---

## 👨‍💻 Author

**Abhijit**
Python | GenAI | Backend | Systems-Oriented Developer

---

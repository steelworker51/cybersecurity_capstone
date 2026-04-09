# 🛡️ Log Analyzer – "Robot Guard"

## 📌 Overview
A Python-based tool that analyzes system authentication logs to detect suspicious activity.

---

## 🎯 Features
- Detects failed login attempts
- Tracks IP-based activity
- Identifies sudo/root usage
- Generates CSV reports

---

## ⚙️ How It Works
1. Reads auth.log
2. Filters failed attempts
3. Extracts IP addresses
4. Counts occurrences
5. Flags high-risk behavior
6. Outputs report

---

## 📊 Sample Output
SECURITY SUMMARY REPORT
Total lines scanned: 100
Unique IPs flagged: 3
Boss Mode Threats Detected: 2

---

## 📁 Output File
security_report.csv

---

## ▶️ How to Run
1. Place auth.log in directory
2. Run:
python3 log_analyzer.py

---

## 🧠 Skills Demonstrated
- Log analysis
- Python scripting
- Cybersecurity fundamentals

---

## 🏁 Conclusion
Transforms raw logs into actionable security insights.

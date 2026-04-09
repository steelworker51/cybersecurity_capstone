# 🛡️ Python Log Analyzer 
**Created by: Dale Murphy**

## 📝 Project Objective
Develop a Python script that analyzes authentication logs to find suspicious behavior and protect the "castle."

## 🚀 How It Works
My Robot Guard does four main things:
1. **Parses the Log:** It reads the `auth.log` file line-by-line.
2. **Identifies Threats:** It looks for the word "Failed" to find bad login attempts.
3. **Tracks IPs:** It counts how many times each address fails using a Python Dictionary.
4. **Detects Boss Mode:** It flags any attempts to use `sudo` or `root` (Privilege Escalation).

## 📊 Output
- **Console Summary:** A quick report showing total lines scanned and threats found.
- **CSV Export:** It automatically creates a `security_report.csv` file that can be opened in Excel.

## 🛠️ Skills Demonstrated
- File Handling (`with open`)
- String Parsing (`split`)
- Data Structures (Dictionaries and Lists)
- Error Handling (`try/except`)
- Professional Reporting

## 🏃 How to Run
1. Ensure `auth.log` is in the folder.
2. Run the command: `python log_analyzer.py`
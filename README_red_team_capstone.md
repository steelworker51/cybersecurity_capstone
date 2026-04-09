# 🔴 Red Team Lite Capstone Project

## 📌 Overview
This project demonstrates foundational Red Team skills including reconnaissance, enumeration, exploitation attempts, and analysis of system vulnerabilities within a controlled lab environment.

The objective was to simulate real-world attacker behavior while documenting findings and translating technical results into clear, actionable insights.

---

## 🎯 Objectives
- Perform network reconnaissance and identify live hosts
- Discover open ports and exposed services
- Attempt controlled access to systems
- Identify vulnerabilities and misconfigurations
- Document findings in a structured security report

---

## 🛠️ Tools & Techniques Used
- Nmap (Port Scanning & Enumeration)
- SSH (Remote Access Testing)
- Curl (Web Requests / Endpoint Testing)
- OpenVPN (Lab Environment Access)
- Linux CLI (Navigation & Analysis)

---

## 🔍 Key Activities

### 1. Reconnaissance
- Identified internal systems:
  - 172.31.1.31
  - 172.31.1.34
  - 172.31.1.37
- Discovered open port:
  - Port 22 (SSH)

---

### 2. Exploitation Attempts
ssh root@172.31.1.31
ssh admin@172.31.1.34
ssh user@172.31.1.37

Result:
Permission denied (publickey)

---

### 3. Web Application Testing
curl http://172.31.1.252:8080/myorders/8

Finding:
Potential IDOR vulnerability allowing access to unauthorized records.

---

## ⚠️ Identified Vulnerability
Broken Access Control (IDOR)

Impact:
- Unauthorized data exposure
- Privacy violations

Recommendation:
- Require authentication
- Validate user ownership

---

## 🧠 Skills Demonstrated
- Network reconnaissance
- Vulnerability identification
- Command-line proficiency
- Security analysis & reporting

---

## 🏁 Conclusion
This project demonstrates attacker mindset and defensive awareness critical for cybersecurity roles.

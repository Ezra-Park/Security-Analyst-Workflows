# Alert Ticket: A-2703 - SERVER-MAIL Phishing Attempt / Malware Download

---

## 1. Ticket Overview

* **Ticket ID:** A-2703
* **Alert Message:** SERVER-MAIL Phishing attempt possible download of malware
* **Severity:** Medium
* **Details:** The user may have opened a malicious email and opened attachments or clicked links.
* **Ticket Status:** Escalated

---

## 2. Ticket Comments & Analyst Findings

**Analyst:** Ezra Park (Simulated)
**Date/Time of Comment:** (Assume current time, e.g., 2025-07-21 15:30:00 EDT)

The alert detected that an employee of Inergy opened and downloaded a malicious attachment from a phishing email.

**Investigation Summary:**

* **Email Suspicion:** The email exhibits clear phishing indicators:
    * Grammatical errors in the "Subject" and "Heading."
    * Inconsistent sender email address ("76tguyhh6tgftrt7tg.su") and name ("Def Communications") compared to the name at the end of the email ("Clyde West").
* **Malicious Attachment Confirmation:**
    * The attached file has a file hash (`54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b`) that matches a known Trojan, specifically `flagpro/fragtor`.
    * This malware is known to be used by the **Advanced Persistent Threat (APT) group known as BlackTech.**
* **Escalation Rationale:** The incident is being escalated as recommended by the Phishing Incident Response Playbook. The Severity is confirmed as Medium due to the successful download of a malicious file, and the confirmed link to a known APT group.

---

## 3. Additional Information / Indicators of Compromise (IOCs)

* **Known Malicious File Hash (SHA256):** `54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b`
* **Malware Family:** Trojan (flagpro/fragtor)
* **Associated Threat Group:** BlackTech (APT)
* **Attachment Filename:** `bfsvc.exe`
* **Password for Attachment:** `paradise10789` (Note: Malicious technique to bypass email filters)

---

## 4. Email Details

```

From: Def Communications \<76tguyhh6tgftrt7tg.su\> \<114.114.114.114\>
Sent: Wednesday, July 20, 2022 09:30:14 AM
To: [hr@inergy.com](mailto:hr@inergy.com) \<176.157.125.93\>
Subject: Re: Infrastructure Egnieer role

Dear HR at Ingergy,

I am writing for to express my interest in the engineer role posted from the website.

There is attached my resume and cover letter. For privacy, the file is password protected. Use the password paradise10789 to open.

Thank you,

Clyde West
Attachment: filename="bfsvc.exe"

```

# Cybersecurity Audit Report: Controls and Compliance Assessment for Botium Toys

**Date of Report:** 2025-07-21 (Current Date)
**Client:** Botium Toys
**Auditor:** Ezra Park (Security Analyst)
**Version:** 1.0

---

## 1. Executive Summary

This report presents the findings of a controls and compliance assessment conducted for Botium Toys. The objective was to evaluate the current state of key security controls and adherence to best practices derived from PCI DSS, GDPR, and SOC principles.

The assessment identified several critical areas where security controls are either absent or require significant improvement, including **Least Privilege, Disaster Recovery Plans, enhanced Password Policies, Separation of Duties, Intrusion Detection Systems (IDS), proper Legacy System Management, Encryption, and a Password Management System**. Additionally, the company shows gaps in compliance adherence, particularly concerning the secure handling of sensitive data (credit card information, EU customer data) and robust user access management.

Implementing the recommended controls and practices is crucial for reducing security risks, protecting sensitive assets (like PII/SPII and credit card data), and strengthening Botium Toys' overall security posture to meet industry best practices and regulatory expectations.

---

## 2. Scope & Objectives

* **Scope:** Assessment of current security controls and compliance with selected best practices for Botium Toys.
* **Objectives:**
    * To identify existing cybersecurity controls and significant gaps.
    * To assess adherence to key compliance best practices (PCI DSS, GDPR, SOC).
    * To provide actionable recommendations for risk reduction and security posture improvement.

## 3. Methodology

This assessment was conducted by utilizing a structured controls and compliance checklist. Information was gathered through:
* Review of existing documentation (where available).
* High-level discussions with relevant IT personnel and stakeholders.
* Assessment against predefined control categories and compliance regulations (referencing external "scope, goals, and risk assessment report" and "control categories document," and "controls, frameworks, and compliance reading" as implied by the source material).

The checklist format allowed for a rapid determination of whether specific controls were in place or compliance best practices were adhered to (Yes/No).

---

## 4. Controls Assessment Checklist

This checklist indicates whether Botium Toys currently has each control in place:

| Control                                                | In Place (Yes) | Not In Place (No) |
| :----------------------------------------------------- | :------------- | :---------------- |
| Least Privilege                                        |                | ●                 |
| Disaster recovery plans                                |                | ●                 |
| Password policies                                      | ●              |                   |
| Separation of duties                                   |                | ●                 |
| Firewall                                               | ●              |                   |
| Intrusion detection system (IDS)                       |                | ●                 |
| Backups                                                | ●              |                   |
| Antivirus software                                     | ●              |                   |
| Manual monitoring, maintenance, & intervention for legacy systems |                | ●                 |
| Encryption                                             |                | ●                 |
| Password management system                             |                | ●                 |
| Locks (offices, storefront, warehouse)                 | ●              |                   |
| Closed-circuit television (CCTV) surveillance          | ●              |                   |
| Fire detection/prevention (fire alarm, sprinkler system, etc.) | ●              |                   |

---

## 5. Compliance Checklist

This checklist indicates whether Botium Toys currently adheres to the specified compliance best practices:

### Payment Card Industry Data Security Standard (PCI DSS)

| PCI DSS Best Practice                                              | Adheres (Yes) | Does Not Adhere (No) |
| :----------------------------------------------------------------- | :------------ | :------------------- |
| Only authorized users have access to customers’ credit card information. |               | ●                    |
| Credit card information is stored, accepted, processed, and transmitted internally, in a secure environment. | ●             |                      |
| Implement data encryption procedures to better secure credit card transaction touchpoints and data. |               | ●                    |
| Adopt secure password management policies.                         |               | ●                    |

### General Data Protection Regulation (GDPR)

| GDPR Best Practice                                                 | Adheres (Yes) | Does Not Adhere (No) |
| :----------------------------------------------------------------- | :------------ | :------------------- |
| E.U. customers’ data is kept private/secured.                      |               | ●                    |
| There is a plan in place to notify E.U. customers within 72 hours if their data is compromised/there is a breach. | ●             |                      |
| Ensure data is properly classified and inventoried.                |               | ●                    |
| Enforce privacy policies, procedures, and processes to properly document and maintain data. | ●             |                      |

### System and Organizations Controls (SOC type 1, SOC type 2)

| SOC Best Practice                                                  | Adheres (Yes) | Does Not Adhere (No) |
| :----------------------------------------------------------------- | :------------ | :------------------- |
| User access policies are established.                              |               | ●                    |
| Sensitive data (PII/SPII) is confidential/private.                 |               | ●                    |
| Data integrity ensures the data is consistent, complete, accurate, and has been validated. | ●             |                      |
| Data is available to individuals authorized to access it.          | ●             |                      |

---

## 6. Key Findings & Recommendations Summary

Based on the controls and compliance checklists, the following key recommendations are made to the IT manager to communicate to stakeholders to reduce risks to assets and improve Botium Toys’ security posture:

### Control Implementation Recommendations:

To significantly improve Botium Toy’s security posture, it is recommended to implement or enhance the following controls:

* **Least Privilege:** Ensure users and systems are granted only the minimum necessary access to perform their functions. This directly addresses gaps in user access control.
* **Disaster Recovery Plan (DRP):** Develop and regularly test a comprehensive DRP to ensure business continuity and data recovery in the event of a major disruption.
* **Improved Password Policies & Management:** Strengthen existing password policies to include higher complexity, regular rotation, and implement a centralized password management system to securely store and manage credentials.
* **Separation of Duties (SoD):** Implement and enforce SoD principles for critical functions to prevent a single individual from performing, or being able to perform, actions that could compromise security or financial integrity.
* **Intrusion Detection System (IDS):** Deploy an IDS to monitor network traffic and system activity for malicious patterns or anomalies, enhancing threat detection capabilities.
* **Improved Ongoing Legacy System Management:** Establish robust manual monitoring, maintenance, and intervention procedures specifically for legacy systems that cannot be easily updated or replaced, to mitigate their inherent vulnerabilities.
* **Encryption:** Implement comprehensive encryption for data at rest and in transit, especially for sensitive customer and internal data, to protect confidentiality.
* **Password Management System:** Adopt a dedicated system to manage employee passwords securely, promoting strong password practices and reducing reliance on insecure methods.

### Compliance Mitigation Recommendations:

To mitigate risks regarding compliance, Botium Toys must focus on the following key areas:

* **Access Control for Sensitive Data:** Implement robust controls, including **Least Privilege** and **Separation of Duties**, to ensure that only authorized users have access to customers’ credit card information and other sensitive data (PII/SPII).
* **Data Encryption:** Enhance **Encryption** procedures to better secure credit card transaction touchpoints and data, as well as ensure the privacy and security of E.U. customers' data.
* **Data Classification and Inventory:** **Properly classify and inventory all assets**, especially those containing sensitive data (PII/SPII). This foundational step will enable the identification and implementation of additional, targeted controls to protect confidential data, ultimately leading to a stronger overall security posture.

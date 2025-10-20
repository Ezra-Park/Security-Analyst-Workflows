# LastPass Standard Operating Procedure (SOP) - InfoSec Department Sample

*Version: 1.1 (InfoSec Specific - Sample)*
*Date: 2025-10-18*
*Author: Ezra Park*
*Approval: [Approving Authority]*

---

## 1. Purpose

This SOP defines standard procedures for an Information Security (InfoSec) department's use of LastPass for managing individual and shared organizational credentials. It ensures consistent, secure practices in handling sensitive access information critical to departmental functions.

## 2. Scope

This SOP applies to all members of the [Organization] InfoSec department utilizing LastPass for work-related credential management.

## 3. Core Security Mandates (Non-Negotiable)

* **Master Password Confidentiality & Strength:** Your LastPass Master Password **MUST** adhere to the [Organization's Password Policy] regarding length and complexity. It must be unique and **NEVER** shared, written down, or stored insecurely. Compromise of an InfoSec team member's Master Password constitutes a high-severity security incident.
* **MFA Enforcement:** Multi-Factor Authentication (MFA) **MUST** be enabled on all InfoSec LastPass accounts using approved methods ([List Approved MFA Methods, e.g., Authenticator App, Security Key]).
* **Approved Sharing Only:** Use **only** LastPass's built-in secure sharing features (Shared Folders, individual item sharing with appropriate permissions) for distributing credentials within the team or organization. Manually copying/pasting credentials, especially for shared or master accounts, is **strictly prohibited** unless explicitly documented for a specific, temporary, audited purpose.
* **Regular Auditing:** Team members are expected to periodically review their Vault access logs and shared folder permissions for any anomalies.

## 4. Account Setup & Configuration

1.  **Provisioning:** Accounts are provisioned by [Designated Administrator or Process].
2.  **Browser Extension:** Ensure the official LastPass browser extension is installed and enabled on all approved work browsers ([List Approved Browsers]).
3.  **MFA Setup:** Configure MFA immediately upon first login using the [Internal MFA Setup Guide].
4.  **Recovery Options:** Configure **all available** LastPass account recovery methods (e.g., mobile recovery, recovery OTPs, password hint *used securely*). Ensure these are kept up-to-date.

## 5. Logging Into LastPass

1.  Use the browser extension or navigate to [https://lastpass.com](https://lastpass.com).
2.  Enter your official [Organizational Email Format] email address.
3.  Enter your unique Master Password.
4.  Complete MFA verification.

## 6. Managing Credentials in Your Vault

1.  **Adding Credentials:** Utilize the browser extension prompt to save credentials upon first login to a new site/service. Manually add credentials only when necessary, ensuring accuracy of URL, username, and password fields. *(Screenshot location: Example of adding an item, highlighting URL/username/password fields)*
2.  **Organization:** Store credentials logically using LastPass Folders. Adhere to the [Departmental Folder Structure] standard. Tagging may be used for cross-referencing.
3.  **Sensitive Information:** Do not store highly sensitive data unrelated to login credentials (e.g., private encryption keys, extensive personal notes) within LastPass notes fields unless explicitly approved and necessary for the credential's use. Use the [Approved Secrets Management Tool] where appropriate.

## 7. Using Credentials (Securely)

1.  **Primary Method (Extension Auto-Fill):** Navigate to the login page. Click within the credential fields and select the appropriate entry from the LastPass extension prompt.
2.  **Secondary Method (Extension Copy):** If auto-fill fails, use the "Copy Password" or "Copy Username" function directly from the browser extension icon. Avoid manually revealing and copying passwords where possible to minimize exposure. *(Screenshot location: Copy Password option in extension)*

## 8. Accessing & Managing Shared Credentials

1.  **Shared Folders:** Access team-shared credentials via the "Sharing Center" -> "Shared Folders" section in your Vault or designated folders within the extension. Permissions are managed by the [Designated Administrator or Role].
2.  **Individual Shares:** Accept or reject credentials shared directly with you via the "Sharing Center".
3.  **Requesting Access:** To request access to credentials not currently shared with you, submit a request via the [Designated Ticketing System or Process] detailing the required credential and business justification.
4.  **Sharing Credentials:** When sharing credentials (if authorized), **always** use the principle of least privilege. Grant "Read Only" access unless write access is explicitly required and approved. Set expiration dates for temporary shares where applicable. **NEVER** share credentials outside of LastPass.

## 9. Master Password Recovery (InfoSec Procedure)

1.  **Self-Service First:** Exhaust **all** configured LastPass self-service recovery options (Mobile Recovery, Recovery OTPs, Hint, SMS). Document attempts.
2.  **Internal Escalation:** If self-service fails, contact the [Designated LastPass Administrator(s)] via the [Designated Secure Communication Channel] detailing the issue and steps taken. **Do not** use general IT helpdesk channels for InfoSec Master Password issues.
3.  **Admin Recovery:** The designated Admin will follow the internal procedure for verifying identity and initiating an administrative recovery, if possible and warranted. This process will be logged.
4.  **Account Reset (Last Resort):** If administrative recovery is impossible, a full account reset may be required, potentially resulting in vault data loss if not previously backed up securely (e.g., secure export).

## 10. Auditing & Reporting

1.  **Personal Audits:** Periodically review "Account Settings" -> "Show Advanced Settings" -> "History" and "Login History" for suspicious activity. Review items shared *by* you in the Sharing Center.
2.  **Reporting Issues:** Report any suspected compromise, policy violations, or suspicious activity related to LastPass immediately to the [InfoSec Incident Response Process].

## 11. Support

For procedural questions or non-urgent technical issues with LastPass, consult the [Internal Knowledge Base] or contact the [InfoSec Team Support Channel].

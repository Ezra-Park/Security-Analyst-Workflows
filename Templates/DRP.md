# Disaster Recovery Plan (DRP)

**Compliance:** NIST SP 800-34 Rev. 1, NIST SP 800-53 CP-1 through CP-10

---

## 1. Purpose

This Disaster Recovery Plan (DRP) ensures the rapid recovery of critical systems, applications, and infrastructure following a disruption or disaster.

---

## 2. Scope

Applies to all mission-critical systems managed by the organization, including cloud-based, on-prem, and third-party hosted systems.

---

## 3. Objectives

- Restore critical business operations within RTO/RPO limits.
- Protect data integrity and confidentiality.
- Minimize financial and operational damage.
- Meet regulatory and service-level commitments.

---

## 4. Business Impact Analysis Summary

| System | Recovery Time Objective (RTO) | Recovery Point Objective (RPO) |
|--------|-------------------------------|--------------------------------|
| Email  | 4 hours                       | 15 minutes                     |
| ERP    | 8 hours                       | 1 hour                         |
| SIEM   | 2 hours                       | 15 minutes                     |

---

## 5. Types of Disasters Covered

- Cyber attacks (e.g., ransomware, DDoS)
- Natural disasters (flood, fire, earthquake)
- Power outages and hardware failure
- Insider threats or sabotage
- Cloud provider downtime

---

## 6. Recovery Procedures

### a. Activation

- Declare disaster and notify DR team
- Activate DR communication plan
- Assess extent of damage

### b. Backup and Restoration

- Restore systems from validated offsite/cloud backups
- Prioritize by criticality
- Verify data integrity before go-live

### c. Rebuilding

- Reinstall operating systems, applications
- Harden configurations (CIS/STIG)
- Patch and validate systems

### d. Verification and Testing

- Test all systems for full functionality
- Monitor systems for signs of reinfection or failure
- Sign-off by leadership before resuming operations

---

## 7. Roles and Responsibilities

| Role              | Responsibility                                 |
|-------------------|------------------------------------------------|
| DR Coordinator    | Oversees DR plan execution and communications |
| IT Infrastructure | Restores systems and applies security configs |
| Compliance        | Coordinates reporting and audits               |
| Business Unit Lead| Validates application recovery                 |

---

## 8. Testing and Maintenance

- Annual full DR simulation
- Quarterly backup restore tests
- Biannual DR documentation updates
- Vendor and contact list review every 6 months

---

## 9. Plan Storage & Access

- Secure offline and cloud storage
- Access restricted to authorized personnel
- Emergency credentials stored securely

---

## 10. References

- [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)
- [NIST SP 800-53 Rev. 5 - CP Controls](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)

# SQL Security Log Analysis: Applying Filters to Queries

## Project Overview

This project demonstrates the application of Structured Query Language (SQL) for investigating potential security issues by efficiently retrieving relevant information from large datasets. SQL enables quick and thorough analysis of logs and other structured data to identify anomalies, track suspicious activity, and support incident response efforts.

## Scenario & Objective

The primary objective is to showcase that SQL operators and clauses can be used to filter and extract specific records from simulated security-related databases, mirroring tasks performed in a Security Operations Center (SOC) or IT security role. We use sample tables such as `log_in_attempts` and `employees` to demonstrate common filtering needs.

## Query Examples & Demonstrations

### 1. Retrieve After-Hours Failed Login Attempts

**Scenario:** We need to investigate failed login attempts that occurred outside of standard business hours to identify potential unauthorized activity. Specifically, we'll identify all unsuccessful login attempts made after 18:00 (6 PM).

**Objective:** Parse the `log_in_attempts` table to find records where the `time` is greater than `18:00` AND the `success` value is `0` (indicating a failed attempt). MySQL stores Boolean `FALSE` as `0`.

**SQL Query:**

<img width="577" height="335" alt="image" src="https://github.com/user-attachments/assets/c276246b-e5e7-4d5c-ae83-30a2e49d9975" />


### 2. Retrieve Login Attempts on Specific Dates

**Scenario:** A suspicious event was reported on '2022-05-09'. We need to retrieve all login attempts that occurred on this specific day and the day immediately preceding it to understand the full context of activity.

**Objective:** Gather login attempt data for '2022-05-09' and '2022-05-08' from the `log_in_attempts` table. This can be achieved using either the `OR` operator or the `BETWEEN` operator in the `WHERE` clause.

**SQL Query (OR Operator):**

<img width="577" height="323" alt="image" src="https://github.com/user-attachments/assets/6b77170e-afef-4caf-a6d5-d138f74179b8" />

`OR` allows us to search for data that matches either condition mentioned above.

**SQL Query (BETWEEN Operator):**

<img width="577" height="325" alt="image" src="https://github.com/user-attachments/assets/93208a75-b6c5-4380-bc91-c91485680b6d" />

`BETWEEN` works in this case because it is an inclusive operator, meaning it includes the dates that we are using to filter.

### 3. Retrieve Login Attempts from Specific Geos (Exclusion)

**Scenario:** Our team is investigating login attempts that did not originate from our primary operating country, Mexico, as these could represent external threats or policy violations.

**Objective:** Filter the `log_in_attempts` table to exclude all results where the country field starts with 'MEX'. The `LIKE` operator with the wildcard `%` helps to filter out variations such as 'MEX' or 'MEXICO'.

**SQL Query:**

<img width="577" height="430" alt="image" src="https://github.com/user-attachments/assets/f7797e56-212b-4556-9411-8691ea768216" />

### 4. Filter Employee Data for Specific Departments and Locations

**Scenario:** We need to identify employees in the Marketing department who are located in any of our 'East' office buildings to coordinate a specific security update. This requires combining multiple conditions.

**Objective:** Retrieve employee information from the `employees` table, filtering for `department = 'Marketing' AND office_location LIKE 'East%'`.

**SQL Query (AND Operator):**

<img width="577" height="246" alt="image" src="https://github.com/user-attachments/assets/1cafa481-5963-42f8-8ef6-fa963c9f6fce" />

When we want to filter results that match two conditions, the `AND` operator allows us to string together more than one condition, such as a department filter and an office filter.

### 5. Retrieve Employees from Specific Departments (Inclusion)

**Scenario:** Our team needs to perform a targeted security update for employees in either the Finance or Sales departments.

**Objective:** Locate information on all employees whose department is either 'Finance' or 'Sales' from the `employees` table.

**SQL Query (OR Operator):**

<img width="577" height="406" alt="image" src="https://github.com/user-attachments/assets/9bb45d5f-97d0-4589-a51e-57291b80c9d5" />

### 6. Retrieve All Employees NOT in a Specific Department (Exclusion)

**Scenario:** A specific security update has already been applied to employee computers in the IT department. We now need to gather information on all other employees to schedule their updates.

**Objective:** Exclude employees from the 'Information Technology' department from the `employees` table. This can be achieved using various exclusion operators.

**SQL Query (<> Operator):**

<img width="577" height="430" alt="image" src="https://github.com/user-attachments/assets/aca45b64-6cc5-4879-9aa9-1113c7518cd1" />

**SQL Query (!= Operator):**

<img width="577" height="423" alt="image" src="https://github.com/user-attachments/assets/72a8be41-c15c-4706-aa65-656908a84675" />

**SQL Query (NOT Operator):**

<img width="577" height="426" alt="image" src="https://github.com/user-attachments/assets/00598065-1c49-4710-adab-4a1fdf6bdcae" />

## Summary

In these examples, we've navigated through simulated databases to return desired information based on specific conditions relevant to cybersecurity investigations. The effective use of SQL operators (e.g., `AND`, `OR`, `BETWEEN`, `LIKE`, `NOT`) and a foundational understanding of basic SQL query components (`SELECT`, `FROM`, `WHERE`) are critical tools. These skills enable cybersecurity professionals to discern relevant information quickly and thoroughly, supporting threat detection, incident response, and security posture management.

## Connect

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/ezra-park-779325330/) if you have any questions or feedback.

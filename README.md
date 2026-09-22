# IT Support Ticket Automation

> A Python-based automation system for validating, processing, routing, and reporting IT support tickets.

## Overview

**IT Support Ticket Automation** is a Python application that automates common IT support ticket processing tasks.

The system takes ticket information from a CSV file, validates the submitted data, identifies duplicate requests, assigns tickets to the appropriate support team, calculates SLA deadlines based on priority, and generates structured processing reports.

The project demonstrates how repetitive IT service-management workflows can be automated using **Python, data validation, business rules, and file-based data processing**.

---

## Key Features

- Ticket data validation
- Email format validation
- Priority validation
- Issue-type validation
- Duplicate ticket detection
- Automatic ticket ID generation
- Rule-based team assignment
- Priority-based SLA calculation
- Invalid-ticket rejection with reasons
- Processed and rejected ticket separation
- Automated summary reporting

---

## Workflow

```text
                Input Tickets
                     │
                     ▼
              Data Normalization
                     │
                     ▼
               Data Validation
                     │
          ┌──────────┴──────────┐
          │                     │
       Valid                 Invalid
          │                     │
          ▼                     ▼
   Duplicate Check        Rejection Reason
          │
     ┌────┴────┐
     │         │
  Unique   Duplicate
     │         │
     ▼         ▼
Team Routing  Reject
     │
     ▼
SLA Calculation
     │
     ▼
Processed Tickets
     │
     ▼
Summary Report
```

---

## Business Rules

### Ticket Validation

The system validates:

- Email format
- Priority
- Issue type
- Required ticket information

Invalid tickets are rejected with a corresponding reason.

### Duplicate Detection

Tickets with the same email and issue type within a **24-hour window** are treated as duplicates.

### Team Routing

Tickets are automatically assigned based on their issue type:

| Issue Type | Assigned Team |
|---|---|
| WiFi | Network |
| Login | IT Support |
| Software | Applications |
| Hardware | Infrastructure |
| Other | General |

### SLA Calculation

SLA deadlines are calculated from the ticket timestamp and priority:

| Priority | SLA |
|---|---:|
| High | 4 hours |
| Medium | 24 hours |
| Low | 72 hours |

**Formula:**

```text
SLA Deadline = Ticket Timestamp + SLA Duration
```

---

## Input

The application reads ticket information from a CSV file.

### Example

| Ticket ID | Name | Email | Issue Type | Priority | Description | Timestamp |
|---|---|---|---|---|---|---|
| 101 | Rahul | rahul@example.com | WiFi | High | WiFi not working | 2026-03-09 09:00:00 |

---

## Output

The system produces three primary outputs.

### Processed Tickets

Contains validated tickets along with:

- Assigned support team
- SLA deadline
- Cleaned ticket information

### Rejected Tickets

Contains tickets that failed validation or duplicate checks, together with the reason for rejection.

Possible rejection reasons include:

- Invalid email
- Invalid priority
- Unknown issue type
- Duplicate ticket

### Summary Report

Provides an overview of the processing results, including:

- Total tickets received
- Successfully processed tickets
- Rejected tickets
- Processing ratio
- Tickets assigned to each support team

---

## Project Structure

```text
it-support-ticket-automation/
│
├── automation.py
├── tickets.csv
├── processed_tickets.csv
├── rejected_tickets.csv
├── summary_report.csv
├── README.md
├── LICENSE
└── .gitignore
```

---

## Technologies

- **Python**
- **CSV Processing**
- **Regular Expressions**
- **Datetime Processing**
- **Rule-Based Automation**

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Harshakiran08/it-support-ticket-automation.git
cd it-support-ticket-automation
```

### 2. Run the application

Make sure `tickets.csv` is available in the project directory.

```bash
python automation.py
```

### 3. Review the generated reports

After execution, the application generates:

```text
processed_tickets.csv
rejected_tickets.csv
summary_report.csv
```

---

## Example Use Case

Consider an organization receiving hundreds of IT support requests every day.

Instead of manually checking every request:

```text
Incoming Ticket
      ↓
Validate
      ↓
Check Duplicate
      ↓
Determine Issue Type
      ↓
Assign Support Team
      ↓
Calculate SLA
      ↓
Generate Report
```

The automation reduces repetitive processing and creates a consistent, rule-based workflow for handling incoming support tickets.

---

## What This Project Demonstrates

This project demonstrates practical experience with:

- Python automation
- Data validation
- Business-rule implementation
- File-based data processing
- Exception and error handling
- Duplicate detection
- Rule-based classification
- SLA management
- Automated reporting

---

## Future Improvements

Potential extensions include:

- REST API integration
- Database-backed ticket storage
- Web-based ticket dashboard
- Email notifications
- Authentication and role-based access
- Configurable SLA rules
- Automated ticket prioritization
- Machine-learning based ticket classification
- Integration with IT service-management platforms

---

## Author

**Harsha Kiran H B**

B.E. Information Science & Engineering

[GitHub](https://github.com/Harshakiran08)

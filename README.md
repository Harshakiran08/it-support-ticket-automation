# IT Support Ticket Automation

## Overview
This project implements an automated system for processing IT support tickets using Python. The automation reads ticket data from a CSV file, validates and cleans the data, removes duplicate tickets, routes each ticket to the appropriate IT support team, calculates SLA deadlines, and generates summary reports.

The purpose of this automation is to reduce manual effort in managing IT support requests, improve ticket routing accuracy, and provide clear insights into ticket processing through automated reporting.

---

## Features

- Email format validation
- Priority validation (Low, Medium, High)
- Issue type validation
- Duplicate ticket detection within 24 hours
- Automatic ticket ID generation if missing
- Ticket routing to appropriate IT teams
- SLA deadline calculation based on priority
- Error handling for invalid tickets
- Storage failure handling
- Summary report generation

---

## Input Data

The automation uses a CSV file as input containing support ticket data.

Input file:

```
tickets.csv
```

Example structure:

| Ticket ID | Name | Email | Issue Type | Priority | Description | Timestamp |
|-----------|------|------|-----------|---------|-------------|-----------|
| 101 | Rahul | rahul@gmail.com | wifi | High | Wifi not working | 2026-03-09 09:00:00 |

---

## Automation Workflow

1. Load ticket data from the CSV file.
2. Normalize text fields (convert to lowercase and remove extra spaces).
3. Validate email format.
4. Validate priority values.
5. Validate issue type.
6. Detect duplicate tickets (same email and issue within 24 hours).
7. Generate a ticket ID if it is missing.
8. Assign the ticket to the appropriate support team.
9. Calculate the SLA deadline based on priority.
10. Store processed tickets and rejected tickets.
11. Generate a summary report.

---

## Routing Rules

| Issue Type | Assigned Team |
|------------|---------------|
| wifi | Network |
| login | IT Support |
| software | Applications |
| hardware | Infrastructure |
| other | General |

---

## SLA Rules

| Priority | SLA Duration |
|----------|--------------|
| High | 4 hours |
| Medium | 24 hours |
| Low | 72 hours |

SLA Deadline Formula:

```
SLA Deadline = Ticket Timestamp + SLA Duration
```

---

## Output Files

### Processed Tickets

```
processed_tickets.csv
```

Contains cleaned and validated tickets including:
- Assigned team
- SLA deadline

---

### Rejected Tickets

```
rejected_tickets.csv
```

Contains tickets rejected due to:
- Invalid email
- Invalid priority
- Unknown issue type
- Duplicate ticket

Each rejected ticket includes the reason for rejection.

---

### Summary Report

```
summary_report.csv
```

The summary report includes:

- Total tickets received
- Processed tickets
- Rejected tickets
- Processed vs rejected ratio
- Tickets assigned to each support team

Example:

| Metric | Value |
|------|------|
| Total Tickets Received | 10 |
| Processed Tickets | 7 |
| Rejected Tickets | 3 |
| Processed vs Rejected | 7 : 3 |
| Network Tickets | 2 |

---

## Project Structure

```
it-support-ticket-automation
│
├── automation.py
├── tickets.csv
│
├── outputs
│   ├── processed_tickets.csv
│   ├── rejected_tickets.csv
│   └── summary_report.csv
│
├── docs
│   └── automation_report.pdf
│
└── README.md
```

---

## How to Run the Project

1. Clone the repository or download the project.

2. Ensure the input file `tickets.csv` is present in the project folder.

3. Run the Python script:

```
python automation.py
```

4. After execution, the following output files will be generated:

- `processed_tickets.csv`
- `rejected_tickets.csv`
- `summary_report.csv`

---

## Technologies Used

- Python
- CSV file processing
- Regular expressions
- Datetime module

---

## Author

Harsha Kiran H B  
BE Information Science & Engineering

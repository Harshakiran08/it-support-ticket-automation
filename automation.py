import csv
import re
from datetime import datetime, timedelta

processed = []
rejected = []
seen = {}

# Routing rules
routing = {
    "wifi": "Network",
    "login": "IT Support",
    "software": "Applications",
    "hardware": "Infrastructure",
    "other": "General"
}

# SLA rules (hours)
sla = {
    "high": 4,
    "medium": 24,
    "low": 72
}

# Email validation
def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Generate unique ticket ID
def generate_id():
    return "TICKET-" + str(int(datetime.now().timestamp()))

# Team ticket counters
team_count = {
    "Network": 0,
    "IT Support": 0,
    "Applications": 0,
    "Infrastructure": 0,
    "General": 0
}

# Read ticket data
with open("tickets.csv", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        # Normalize text fields
        email = row["Email"].lower().strip()
        issue = row["Issue Type"].lower().strip()
        priority = row["Priority"].lower().strip()

        # Email validation
        if not valid_email(email):
            row["Reason"] = "Invalid Email"
            rejected.append(row)
            continue

        # Priority validation
        if priority not in sla:
            row["Reason"] = "Invalid Priority"
            rejected.append(row)
            continue

        # Issue type validation
        if issue not in routing:
            row["Reason"] = "Unknown Issue Type"
            rejected.append(row)
            continue

        timestamp = datetime.strptime(row["Timestamp"], "%Y-%m-%d %H:%M:%S")

        key = (email, issue)

        # Deduplicate within 24 hours
        if key in seen and (timestamp - seen[key]) < timedelta(hours=24):
            row["Reason"] = "Duplicate Ticket"
            rejected.append(row)
            continue

        seen[key] = timestamp

        # Ticket ID generation if missing
        ticket_id = row["Ticket ID"]
        if ticket_id == "":
            ticket_id = generate_id()

        # Routing
        team = routing[issue]

        # SLA deadline calculation
        deadline = timestamp + timedelta(hours=sla[priority])

        # Update ticket fields
        row["Ticket ID"] = ticket_id
        row["Assigned Team"] = team
        row["SLA Deadline"] = deadline

        processed.append(row)

        # Count tickets per team
        team_count[team] += 1


# -----------------------------
# Save Processed & Rejected Tickets
# -----------------------------

try:

    # Processed tickets
    if processed:
        with open("processed_tickets.csv", "w", newline="") as file:

            fieldnames = processed[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(processed)

    # Rejected tickets
    if rejected:
        with open("rejected_tickets.csv", "w", newline="") as file:

            fieldnames = rejected[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(rejected)

except Exception as e:

    print("Storage failure occurred while writing ticket files.")
    print("Error:", e)


# -----------------------------
# Generate Summary Report
# -----------------------------

total = len(processed) + len(rejected)
processed_count = len(processed)
rejected_count = len(rejected)

summary = [
    ["Total Tickets Received", total],
    ["Processed Tickets", processed_count],
    ["Rejected Tickets", rejected_count],
    ["Processed vs Rejected", f"{processed_count} : {rejected_count}"],
    ["Network Tickets", team_count["Network"]],
    ["IT Support Tickets", team_count["IT Support"]],
    ["Applications Tickets", team_count["Applications"]],
    ["Infrastructure Tickets", team_count["Infrastructure"]],
    ["General Tickets", team_count["General"]]
]

try:

    with open("summary_report.csv", "w", newline="") as file:

        writer = csv.writer(file)
        writer.writerow(["Metric", "Value"])

        for row in summary:
            writer.writerow(row)

except Exception as e:

    print("Storage failure occurred while writing summary report.")
    print("Error:", e)


print("Automation completed successfully.")
print("Processed tickets:", processed_count)
print("Rejected tickets:", rejected_count)
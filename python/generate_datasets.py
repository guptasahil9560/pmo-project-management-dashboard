import pandas as pd

# ----------------------------
# 1. PROJECT MASTER DATASET
# ----------------------------
project_data = {
    "Project_ID": ["P001", "P002", "P003", "P004", "P005"],
    "Project_Name": [
        "Vendor Onboarding System",
        "Manufacturing Workflow Automation",
        "Inventory Tracking Upgrade",
        "Quality Audit Dashboard",
        "Order Processing Optimization"
    ],
    "Start_Date": [
        "2025-01-01",
        "2025-02-10",
        "2025-01-15",
        "2025-03-01",
        "2025-02-20"
    ],
    "End_Date": [
        "2025-03-15",
        "2025-06-30",
        "2025-04-20",
        "2025-05-15",
        "2025-04-30"
    ],
    "Project_Manager": [
        "Ramesh Singh",
        "Priya Mehta",
        "Manish Kumar",
        "Ayesha Khan",
        "Deepak Sharma"
    ],
    "Status": ["On Track", "Delayed", "On Track", "High Risk", "On Track"]
}

project_df = pd.DataFrame(project_data)
project_df.to_excel("../data/project_master.xlsx", index=False)


# ----------------------------
# 2. TASKS DATASET
# ----------------------------
tasks_data = {
    "Task_ID": ["T001", "T002", "T003", "T004", "T005", "T006", "T007", "T008"],
    "Project_ID": ["P001", "P001", "P002", "P002", "P003", "P003", "P004", "P005"],
    "Task_Name": [
        "Define Requirements", "Vendor Review Meetings",
        "Process Mapping", "Automation Build",
        "Inventory Data Cleanup", "Integration Testing",
        "Field Audit Checklists", "Order Data Validation"
    ],
    "Owner": [
        "Ravi Kumar", "Neha Sharma", "Suresh Patel", "Amit Verma",
        "Meenakshi Rao", "Arvind Singh", "Sunil Jha", "Ritu Sharma"
    ],
    "Due_Date": [
        "2025-01-15", "2025-02-10", "2025-03-15", "2025-05-20",
        "2025-02-28", "2025-03-20", "2025-03-25", "2025-03-15"
    ],
    "Status": [
        "Completed", "On Track", "Delayed", "On Track",
        "On Track", "On Track", "High Risk", "On Track"
    ],
    "Completion_Percent": [100, 80, 40, 30, 60, 20, 10, 50]
}

tasks_df = pd.DataFrame(tasks_data)
tasks_df.to_csv("../data/tasks.csv", index=False)


# ----------------------------
# 3. RAID LOG DATASET
# ----------------------------
raid_data = {
    "RAID_ID": ["R001", "R002", "R003", "R004", "R005"],
    "Project_ID": ["P002", "P004", "P001", "P005", "P003"],
    "Type": ["Risk", "Issue", "Dependency", "Issue", "Risk"],
    "Description": [
        "RPA Bot Failure Risk",
        "Delayed Vendor Response",
        "Vendor API Pending",
        "Incorrect Order Mapping",
        "Data Quality Concern"
    ],
    "Owner": ["Priya Mehta", "Sunil Jha", "Ravi Kumar", "Ritu Sharma", "Arvind Singh"],
    "Severity": ["High", "Medium", "High", "Low", "Medium"],
    "Status": ["Open", "Open", "Open", "Closed", "Open"]
}

raid_df = pd.DataFrame(raid_data)
raid_df.to_csv("../data/raid_log.csv", index=False)

print("✔ All datasets generated in /data folder!")

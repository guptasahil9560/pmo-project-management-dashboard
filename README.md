# 📊 PMO Project Management Dashboard
A complete end-to-end project management analytics system using Python, SQL, and Power BI.

---

## 🚀 Project Overview
This project delivers a full PMO (Project Management Office) reporting and analytics solution with:
- Automated dataset generation  
- Weekly PDF reporting  
- SQL script generation  
- Power BI executive dashboard  
- Trend snapshots  
- Realistic PMO datasets  

It demonstrates practical project management analytics for:
- Project Coordinator / PMO Analyst  
- Business Analyst  
- MIS / Reporting Analyst  
- Data Analytics roles  

---

## 🧱 Project Structure
pmo-project-management-dashboard/  
│  
├── data/  
│   ├── project_master.csv  
│   ├── tasks.csv  
│   ├── raid_log.csv  
│   └── snapshots/  
│  
├── powerbi/  
│   └── PMO_Dashboard.pbix  
│  
├── sql/  
│   ├── project_master.sql  
│   ├── tasks.sql  
│   └── raid_log.sql  
│  
├── python/  
│   ├── generate_datasets.py  
│   └── weekly_review_report.py  
│  
├── output/  
│   └── weekly_review_report.pdf  
│  
└── README.md  

---

## ⚙️ Features

### 1️⃣ Automated Dataset Generation
The script `generate_datasets.py` automatically creates:
- Project Master dataset  
- Tasks dataset  
- RAID Log  
- Daily snapshots  
- SQL scripts  

Run command:  
python3 python/generate_datasets.py

---

### 2️⃣ Weekly Summary PDF Report
`weekly_review_report.py` generates a professional PMO weekly report:
- Project summary  
- RAG status  
- High-risk & delayed projects  
- RAID overview  
- Deadlines  

Run command:  
python3 python/weekly_review_report.py  

Output PDF: output/weekly_review_report.pdf

---

### 3️⃣ Power BI Executive Dashboard
Interactive dashboard includes:
- Portfolio overview  
- RAG heat map  
- Tasks progress  
- RAID analysis  
- KPI cards  
- Trend charts  

Dashboard file: powerbi/PMO_Dashboard.pbix

---

### 4️⃣ SQL Scripts
Pre-built SQL scripts for analytics:
- project_master  
- tasks  
- raid_log  

Location: sql/

---

## 🛠️ Tech Stack
- Python (pandas, numpy, reportlab)  
- SQL  
- Power BI  
- GitHub Codespaces  
- CSV-based snapshot storage  

---

## 📸 Screenshots
Place screenshots inside the folder:

screenshots/

Suggested screenshots:
- Dashboard overview  
- Task progress  
- RAID log  
- Trend charts  
- Sample weekly report  

---

## 🔮 Future Enhancements
- GitHub Actions automation  
- Email PDF delivery  
- Additional PMO KPIs (SPI, CPI, critical path analysis)  
- Resource allocation dashboard  

---

## 🤝 Contributions
Pull requests and suggestions are welcome.

---

## 📧 Contact
Built by **Sahil Gupta**  
For PMO / Project Coordinator / Business Analyst roles.


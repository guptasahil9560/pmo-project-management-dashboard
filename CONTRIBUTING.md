# Contributing Guide

Thank you for your interest in this project!

## How to run the project

1. Clone the repository:
   git clone https://github.com/guptasahil9560/pmo-project-management-dashboard
   cd pmo-project-management-dashboard

2. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate   (Windows)
   source venv/bin/activate   (Mac/Linux)

3. Install dependencies:
   pip install -r requirements.txt

4. Generate datasets:
   python python/generate_datasets.py --out output/

5. Generate the weekly PDF report:
   python python/weekly_review_report.py --out output/

## How to contribute

- Create a new branch for your update.
- Ensure all scripts run end-to-end without errors.
- Place any new files in the correct folders.
- Update the README if needed.
- Commit your changes with a clear message.
- Open a Pull Request describing what you changed.

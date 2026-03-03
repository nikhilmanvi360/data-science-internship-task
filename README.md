# Data Science Internship: Multi-Task Repository

![Build Status](https://github.com/nikhilmanvi360/data-science-internship-task/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

This repository contains a collection of Data Science internship projects, focused on exploratory data analysis (EDA), predictive modeling, and data visualization.

---

## 🏏 Phase 1: IPL Cricket Data Analytics

Highlights team performance, toss impact, and venue statistics using historical IPL match data.

- **Main Script**: `ipl_analysis.py`
- **Key Visuals**: `01_successful_teams.png`, `02_toss_impact.png`, `03_venue_performance.png`
- **Documentation**: [IPL Project Summary](PROJECT_SUMMARY.txt)

---

## 🎓 Phase 2: Student Score Predictor (ML)

A Linear Regression model designed to predict student exam scores based on study hours. This tool proactively identifies at-risk students by forecasting results.

- **Main Script**: `student_score_predictor.py`
- **Model Results**: R² Score ~0.93
- **Key Visuals**: `eda_plot.png`, `regression_results.png`

---

## 🚀 Quick Start

### 1. Environment Setup

```bash
# Clone the repository
git clone https://github.com/nikhilmanvi360/data-science-internship-task.git
cd data-science-internship-task

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Running the Tools

- **IPL Analysis**:
  ```bash
  python3 ipl_analysis.py
  ```

- **Score Predictor**:
  ```bash
  python3 student_score_predictor.py
  ```

---

## 📂 File Structure

- `requirements.txt` — Project dependencies
- `DATA_DICTIONARY.md` — Detailed explanation of data fields
- `QUICK_START_GUIDE.md` — Extended setup instructions
- `projectoverview.md` — Broad overview of project aims

## 🤝 Contributing
Feel free to open issues or PRs. For formatting and style, follow standard Python conventions.

## 📄 License
MIT

## 📬 Contact
- **GitHub Repository**: [nikhilmanvi360/data-science-internship-task](https://github.com/nikhilmanvi360/data-science-internship-task)

# E-commerce Data Pipeline (PySpark)  
**Name:** Etsubdink Tadesse  
**ID:** DBUR/3971/13  

📌 **Overview**  
This project implements an **end-to-end data pipeline** using **PySpark** and **DuckDB** for processing e-commerce transactions. The pipeline efficiently extracts, transforms, and loads (ETL) data.

---

## 🚀 Project Workflow

1️⃣ **Data Extraction**  
   - Loads raw e-commerce data from a **CSV file** using **PySpark**.

2️⃣ **Data Transformation**  
   - Cleans and preprocesses data, handling missing values and filtering invalid records.  
   - Categorizes transactions based on price into **High, Medium, and Low Value**.

3️⃣ **Data Loading**  
   - Stores transformed data into **DuckDB**, a lightweight OLAP database.

---

## 📂 Directory Structure
├── data/ # Raw and processed datasets ├── scripts/ # Python scripts for ETL pipeline │ ├── extract.py # Extracts data from CSV │ ├── transform.py # Cleans and transforms data │ ├── load.py # Loads data into DuckDB │ ├── notebooks/ # Jupyter notebooks for analysis ├── visualizations/ # Tableau dashboards & insights ├── README.md # Project documentation

---

## ⚙️ How to Run

### 🔹 **Setup Environment**
Ensure Python 3.x is installed, then install dependencies:

```sh
pip install pyspark duckdb
🔹 Run the Pipeline
Execute the ETL pipeline step-by-step:
python3 scripts/extract.py
python3 scripts/transform.py
python3 scripts/load.py



📂 Large Files
Due to size limitations, large files are stored externally. You can download them from the link below:

🔗 Download Large Files





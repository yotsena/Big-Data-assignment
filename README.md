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
📂 Project Directory Structure
├── data/                    # Raw and processed datasets  
├── scripts/                 # Python scripts for ETL pipeline  
│   ├── extract.py           # Extracts data from CSV  
│   ├── transform.py         # Cleans and transforms data  
│   ├── load.py              # Loads data into DuckDB  
│
├── notebooks/               # Jupyter notebooks for analysis  
├── visualizations/          # Tableau dashboards & insights  
├── README.md                # Project documentation  



## 📂 Large Files  

Due to size limitations, large files are stored externally. You can download them from the link below:  

[🔗 Download Large Files](https://drive.google.com/drive/folders/1gJD_VtexnS7mv01XG65GyL3rR3DP8Lpu?usp=sharing)  


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

📊 Data Processing Steps
1️⃣ Handling Missing Values
Column	Action Taken
CustAccountBalance	Filled missing values with 0
CustGender & Brand	Replaced missing values with "Unknown"
2️⃣ Transaction Type Categorization
A new column transaction_type was added based on price range:

Price Range	Category
price > 10000	High Value
1000 < price ≤ 10000	Medium Value
price ≤ 1000	Low Value

3️⃣ Filtering Data
Removed rows where price ≤ 0 (invalid transactions).
📊 Tableau Visualizations
The processed data is visualized using Tableau to derive meaningful insights.

🔗 Key Dashboards:
✅ Sales Trends Over Time
✅ Sales by Location
✅ Transaction Types
✅ Customer Segmentation

🔹 Insights from the Data
📌 Sales peaked in December, likely due to holiday shopping.
📌 Customers in Mumbai contributed the highest revenue.
📌 High-value transactions accounted for 30% of total revenue.











